Reading snapshots with swiftsimio
=================================

The `swiftsimio <https://swiftsimio.readthedocs.io/en/latest/>`__
python module can be used to read snapshots. It can efficiently cut
out regions of interest from the snapshots and handles units and
cosmology metadata. There are two ways to access FLAMINGO data with
swiftsimio:

  * Download a complete snapshot and have swiftsimio read it directly
    using `h5py <https://docs.h5py.org/en/stable/>`__
  * Use swiftsimio to access snapshots stored on `Cosma
    <https://cosma.readthedocs.io/en/latest/>`__ using the `hdfstream
    <https://hdfstream-python.readthedocs.io/en/latest>`__ service

The latter method might be preferable if you only need a small
fraction of the data in a snapshot, such as only certain particle
types or a small region around an object of interest.

Installation
------------

The swiftsimio module can be installed as follows::

  pip install swiftsimio>=12.1.4

For remote access to snapshots we also need the hdfstream module::

  pip install hdfstream

Opening a snapshot
------------------

The examples below show how to open a local HDF5 which you have
downloaded, and how to open a remote file on the hdfstream server.


.. tab-set::

   .. tab-item:: Opening a remote file

      .. code-block:: python

         # Connect to the hdfstream service and open the root directory
         import hdfstream
         root_dir = hdfstream.open("cosma", "/")

         # Open the remote snapshot file
         remote_snapshot = root_dir["FLAMINGO/L1_m10/L1_m10/snapshots/flamingo_0077/flamingo_0077.hdf5"]

         # Pass the remote file object to swiftsimio instead of a filename
         import swiftsimio as sw
         snap = sw.load(remote_snapshot)

   .. tab-item:: Opening a local file

      .. code-block:: python

         import swiftsimio as sw
         snap = sw.load("./FLAMINGO/L1_m10/L1_m10/snapshots/flamingo_0077/flamingo_0077.hdf5")

Each snapshot consists of a large number of data files and a single
:ref:`virtual snapshot file <virtual-snapshot>`. Swiftsimio
should be given the name of the virtual snapshot file, which
references the data in all of the other files.

Snapshot metadata
-----------------

Whether you opened a local or remote snapshot, the ``snap`` object
returned by ``swiftsimio.load`` can be used to access simulation
metadata. The simulation box size is available as::

  snap.metadata.boxsize

The numbers of particles of each type in the snapshot are available as::

  snap.metadata.n_gas
  snap.metadata.n_dark_matter
  snap.metadata.n_stars
  snap.metadata.n_black_holes
  snap.metadata.n_neutrinos

The expansion factor and redshift of the snapshot are also available::

  snap.metadata.a
  snap.metadata.z

To see what particle types exist in this snapshot::

  >>> print(snap)
  SWIFT dataset at /FLAMINGO/L1_m10/L1_m10/snapshots/flamingo_0077/flamingo_0077.hdf5.
  Available groups: gas, dark_matter, stars, black_holes, neutrinos

And to see the particle properties available for one particle type::

  >>> print(snap.dark_matter)
  SWIFT dataset at /FLAMINGO/L1_m10/L1_m10/snapshots/flamingo_0077/flamingo_0077.hdf5.
  Available fields: coordinates, fofgroup_ids, masses, particle_ids, potentials, softenings, velocities

See the `swiftsimio documentation
<https://swiftsimio.readthedocs.io/en/latest/loading_data/index.html#using-metadata>`__
on snapshot metadata for more information.

.. _swiftsimio_cosmology:

Cosmology
---------

If you need cosmology information, you can get an astropy `cosmology
object <https://docs.astropy.org/en/stable/cosmology/index.html>`__ by
opening a snapshot as shown above, then accessing its cosmology
field::

  cosmo = snap.metadata.cosmology

This is the recommended way to translate between redshift, comoving
distance and lookback time in the FLAMINGO simulations. You can
compute the age of the universe at :math:`z = 0.5`, for example,
with::

  age_of_universe = cosmo.age(0.5)

or compute the comoving distance to the same redshift with::

  comoving_distance = cosmo.comoving_distance(0.5)

See the `astropy documentation
<https://docs.astropy.org/en/stable/cosmology/index.html>`__ for more
details.

Reading particle data
---------------------

Particle properties, such as position, mass or velocity, are read in
or downloaded when you try to access them. To read the coordinates of
all star particles in the simulation::

  star_pos = snap.stars.coordinates

If you opened a remote snapshot, this will trigger a download and a
progress bar will appear. The result is a `cosmo_array
<https://swiftsimio.readthedocs.io/en/latest/cosmo_array/index.html>`__,
which is is a numpy array with unit and cosmology information
attached. Units are handled using the `unyt
<https://unyt.readthedocs.io/en/stable/>`__ module. In this example,
the cosmo array records that the particle positions are in comoving
Mpc::

   >>>  print(star_pos)
   [[649.22656783 524.32466783 595.55844783]
   [649.48269783 524.27156783 595.70102783]
   [649.51910783 524.65127783 595.67997783]
   ...
   [987.07861218 995.73119218  88.40002218]
   [987.07806218 995.72685218  88.39880218]
   [987.07910218 995.73126218  88.39935218]] Mpc (Comoving)

.. _swiftsimio_cutouts:

Cutting out a region
--------------------

The particles in Swift snapshots are ordered in a way that allows us
to read regions from a snapshot without reading the entire file. Given
a range of coordinates in x, y, and z, swiftsimio can compute which
parts of the file to read or download to find the corresponding
particles. This is referred to as `spatial masking
<https://swiftsimio.readthedocs.io/en/latest/masking/>`__.

Spatial masking can be used to read in just part of a local snapshot
which you have downloaded, or to download just part of a remote
snapshot on the server.

.. note:: This example has been updated (on 2026-07-17) because
          swiftsimio now requires the coordinates to cut out to be
          specified as a cosmo_array object.

.. tab-set::

   .. tab-item:: Using a remote file

      .. code-block:: python

         # Connect to the hdfstream service and open the root directory
         import hdfstream
         root_dir = hdfstream.open("cosma", "/")

         # Open the remote snapshot file.
         # The path here specifies a file on the server.
         remote_snapshot = root_dir["FLAMINGO/L1_m10/L1_m10/snapshots/flamingo_0077/flamingo_0077.hdf5"]

         # Create a mask object
         import swiftsimio as sw
         mask = sw.mask(remote_snapshot)

         # Define a comoving Mpc unit (this will be simplified in an upcoming swiftsimio version)
         import unyt as u
         cMpc = sw.cosmo_quantity(1.0, u.Mpc, comoving=True, scale_factor=mask.metadata.a, scale_exponent=1)

         # Define the region to read in comoving Mpc
         load_region = [[100*cMpc, 150*cMpc], [100*cMpc, 150*cMpc], [100*cMpc,150*cMpc]]

         # Constrain the region to read
         mask.constrain_spatial(load_region)

         # Open the snapshot using the mask
         snap = sw.load(remote_snapshot, mask=mask)

         # Download the coordinates of gas particles in the region
         gas_pos = snap.gas.coordinates

   .. tab-item:: Using a local file

      .. code-block:: python

         # Name of the snapshot file to open:
         # This is the path to a HDF5 file which we have downloaded.
         filename = "./FLAMINGO/L1_m10/L1_m10/snapshots/flamingo_0077/flamingo_0077.hdf5"

         # Create a mask object
         import swiftsimio as sw
         mask = sw.mask(filename)

         # Define a comoving Mpc unit (this will be simplified in an upcoming swiftsimio version)
         import unyt as u
         cMpc = sw.cosmo_quantity(1.0, u.Mpc, comoving=True, scale_factor=mask.metadata.a, scale_exponent=1)

         # Define the region to read in comoving Mpc
         load_region = [[100*cMpc, 150*cMpc], [100*cMpc, 150*cMpc], [100*cMpc,150*cMpc]]

         # Constrain the region to read
         mask.constrain_spatial(load_region)

         # Open the snapshot using the mask
         snap = sw.load(filename, mask=mask)

         # Read the coordinates of gas particles in the region
         gas_pos = snap.gas.coordinates

Saving a region as a new snapshot
---------------------------------

It's also possible to write a new snapshot file which contains only
the selected region. Using the ``mask`` object from the previous
example::

  sw.subset_writer.write_subset("region_0077.hdf5", mask)

This will write a new HDF5 snapshot file with all particles in the
selected region. This is particularly useful when working with a remote
snapshot because it allows you to download all particles in a region
of interest and save them to a local file so that you don't need to
download them again.
