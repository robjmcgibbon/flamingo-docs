Snapshots
=========

Each FLAMINGO simulation models the evolution of a cubic volume of the
Universe from just after the big bang to the present day. The state of
the simulation is output at intervals as a series of "snapshots",
which record the distribution of particles in the simulated volume at
an instant in time.

Snapshots contain multiple particle types which model different matter
components: cold dark matter (CDM), gas, stars, black holes and
neutrinos. In the dark matter only simulations only CDM and neutrino
particles are present but the CDM particles account for the mass in
baryons, which are assumed to trace the distribution of the CDM. In
the hydro simulations all particle types are present. Many physical
properties, such as position, mass and velocity, are stored for each
particle.

.. card-carousel:: 2

    .. card:: L1_m8 gas temperature at z=0

        .. image:: images/L1_m8_snapshots/L1_m8_gas_temp_z0.jpg

    .. card:: L1_m8 DM velocity dispersion at z=0

        .. image:: images/L1_m8_snapshots/L1_m8_dm_veldisp_z0.jpg

    .. card:: L1_m8 stellar mass at z=0

        .. image:: images/L1_m8_snapshots/L1_m8_stellar_mass_z0.jpg

The following sections describe the layout and contents of the snapshots.

.. toctree::
   :maxdepth: 2

   Directory layout <snapshot_dirs>
   File format <snapshot_format>
   Output redshifts <snapshot_redshifts>
   Particle properties <snapshot_particle_properties>
   Reading with swiftsimio <swiftsimio.rst>
   Reading halo particles <halo_particles.rst>
   Partial snapshots <snapshot_partial>

For more information about the SWIFT simulation snapshot format used
here, see the `SWIFT documentation
<https://swift.strw.leidenuniv.nl/docs/Snapshots/index.html>`__.
