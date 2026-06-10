Reading SOAP halo catalogues with swiftsimio
============================================

The `swiftsimio <https://swiftsimio.readthedocs.io/en/latest/>`__
python module can be used to read SOAP halo catalogues. It can
efficiently cut out regions of interest and handles units and cosmology
metadata. There are two ways to access FLAMINGO data with swiftsimio:

  * Download a complete output and have swiftsimio read it directly
    using `h5py <https://docs.h5py.org/en/stable/>`__
  * Use swiftsimio to access data stored on `Cosma
    <https://cosma.readthedocs.io/en/latest/>`__ using the `hdfstream
    <https://hdfstream-python.readthedocs.io/en/latest>`__ service

The latter method might be preferable if you only need a small
fraction of the data, such as a subset of halo properties or halos in
a small region of interest.

To read the particles associated with a halo selected from a SOAP
catalogue, see :doc:`/snapshots/halo_particles`.

Installation
------------

The swiftsimio module can be installed as follows::

  pip install swiftsimio

For remote access to FLAMINGO outputs we also need the hdfstream module::

  pip install hdfstream

Opening a halo catalogue
------------------------

The examples below show how to open a local HDF5 which you have
downloaded, and how to open a remote file on the hdfstream server.

.. tab-set::

   .. tab-item:: Opening a remote file

      .. code-block:: python

         # Connect to the hdfstream service and open the root directory
         import hdfstream
         root_dir = hdfstream.open("cosma", "/")

         # Open the z=0 halo catalogue fro the L1_m10 simulation
         remote_file = root_dir["FLAMINGO/L1_m10/L1_m10/SOAP-HBT/halo_properties_0077.hdf5"]

         # Pass the remote file object to swiftsimio instead of a filename
         import swiftsimio as sw
         soap = sw.load(remote_file)

   .. tab-item:: Opening a local file

      .. code-block:: python

         import swiftsimio as sw

         # Here we pass the name of the file we downloaded to swiftsimio
         soap = sw.load("./FLAMINGO/L1_m10/L1_m10/SOAP-HBT/halo_properties_0077.hdf5")

Accessing halo properties
-------------------------

SOAP computes halo properties using several different halo
definitions, which are described in :doc:`soap_halo_variations`. We
can see what halo definitions are available in the output we opened
above with::

  >>> print(soap)
  SWIFT dataset at /FLAMINGO/L1_m10/L1_m10/SOAP-HBT/halo_properties_0077.hdf5.
  Available groups: bound_subhalo, exclusive_sphere_1000kpc, exclusive_sphere_100kpc, ...

Similarly, we can find the list of halo properties which are available
for a particular halo definition. If we're interested in properties
evaluated using the particles bound to each subhalo, for example, the
following will return the names of the available properties::

  >>> print(soap.bound_subhalo)
  SWIFT dataset at /FLAMINGO/L1_m10/L1_m10/SOAP-HBT/halo_properties_0077.hdf5.
  Available fields: total_inertia_tensor_noniterative, ... , centre_of_mass, ... , total_mass, ...

The available halo properties are fully documented in
:doc:`soap_property_table`. In this list we can see the centre of mass
of the bound particles, ``centre_of_mass``, and the total bound mass
of the subhalo, ``total_mass``. To read in these quantities::

  pos = snap.bound_subhalo.centre_of_mass
  mass = snap.bound_subhalo.total_mass

Each property is returned as a `cosmo_array
<https://swiftsimio.readthedocs.io/en/latest/cosmo_array/index.html>`__,
which is is a numpy array with unit and cosmology information
attached. Units are handled using the `unyt
<https://unyt.readthedocs.io/en/stable/>`__ module.
