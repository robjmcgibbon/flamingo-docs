SOAP properties table
=====================

The tables below list the (sub)halo properties available within the SOAP catalogues. The first table contains the properties within the ``input_halos`` group.
The second table contains the properties which are calculated for both DMO and HYDRO simulations.
The third table contains the properties which are only calculated for the HYDRO simulations.
The final table contains the datasets copied over from the HBT-HERONS and FoF catalogues.
Within each table the properties are sorted based on their filters.

The first column gives the name of the property when opened using the `swiftsimio library <https://swiftsimio.readthedocs.io/en/latest/soap/index.html>`_. Clicking on each property name will open a dropdown box, which contains information about the dataset within the HDF5 file. The second column gives the filter applied to that property, as described in :doc:`soap_filters`. The third column indicates the halo variations for which this property is available (green if the property is computed for a certain variation, red if not). The variations are as follows:

* ``BS`` - :ref:`bound_subhalo_description`
* ``ES`` - :ref:`exclusive_sphere_description`
* ``IS`` - :ref:`inclusive_sphere_description`
* ``EP`` - :ref:`projected_aperture_description`
* ``SO`` - :ref:`spherical_overdensity_description`

The final column gives a description of the property. Certain properties also contain a link to a footnote at the bottom of this page which gives a full description of how they were calculated.


Input halo properties
---------------------

.. list-table::
   :widths: 25 10 15 50
   :header-rows: 1

   * - Name
     - Filter
     - Variations
     - Description
   * - .. dropdown:: ``input_halos.halo_catalogue_index``

          * **HDF5 name:** ``InputHalos/HaloCatalogueIndex``
          * **Shape:** 1
          * **Type:** int64
          * **Units:** dimensionless
          * **Compression:** no compression
     - basic
     - \-
     - Index of this halo in the original halo finder catalogue (first halo has index=0).
   * - .. dropdown:: ``input_halos.halo_centre``

          * **HDF5 name:** ``InputHalos/HaloCentre``
          * **Shape:** 3
          * **Type:** float64
          * **Units:** :math:`a \cdot \rm{Mpc}`
          * **Compression:** 1 pc accurate
     - basic
     - \-
     - The centre of the subhalo as given by the halo finder. Used as reference for all relative positions. For HBT-HERONS this is equal to the position of the most bound particle in the subhalo.
   * - .. dropdown:: ``input_halos.is_central``

          * **HDF5 name:** ``InputHalos/IsCentral``
          * **Shape:** 1
          * **Type:** int64
          * **Units:** dimensionless
          * **Compression:** no compression
     - basic
     - \-
     - Whether the halo finder flagged the halo as central (1) or satellite (0).
   * - .. dropdown:: ``input_halos.number_of_bound_particles``

          * **HDF5 name:** ``InputHalos/NumberOfBoundParticles``
          * **Shape:** 1
          * **Type:** int64
          * **Units:** dimensionless
          * **Compression:** no compression
     - basic
     - \-
     - Total number of particles bound to the subhalo.

Dark matter only properties
---------------------------

.. list-table::
   :widths: 25 10 15 50
   :header-rows: 1

   * - Name
     - Filter
     - Variations
     - Description
   * - .. dropdown:: ``centre_of_mass``

          * **HDF5 name:** ``CentreOfMass``
          * **Shape:** 3
          * **Type:** float64
          * **Units:** :math:`a \cdot \rm{Mpc}`
          * **Compression:** 1 pc accurate
     - basic
     - :avail:`BS` :avail:`ES` :avail:`IS` :avail:`EP` :avail:`SO`
     - Centre of mass. `[1] <footnote-1_>`_
   * - .. dropdown:: ``centre_of_mass_velocity``

          * **HDF5 name:** ``CentreOfMassVelocity``
          * **Shape:** 3
          * **Type:** float32
          * **Units:** :math:`\rm{km} / \rm{s}`
          * **Compression:** 0.1 km/s accurate
     - basic
     - :avail:`BS` :avail:`ES` :avail:`IS` :avail:`EP` :avail:`SO`
     - Centre of mass velocity. `[1] <footnote-1_>`_
   * - .. dropdown:: ``concentration``

          * **HDF5 name:** ``Concentration``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - basic
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - Halo concentration assuming an NFW profile. Minimum particle radius set to softening length `[2] <footnote-2_>`_
   * - .. dropdown:: ``concentration_unsoftened``

          * **HDF5 name:** ``ConcentrationUnsoftened``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - basic
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - Halo concentration assuming an NFW profile. No particle softening. `[2] <footnote-2_>`_
   * - .. dropdown:: ``dark_matter_mass``

          * **HDF5 name:** ``DarkMatterMass``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`10^{10}\ \rm{M}_\odot`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - basic
     - :avail:`BS` :avail:`ES` :avail:`IS` :avail:`EP` :avail:`SO`
     - Total DM mass.
   * - .. dropdown:: ``enclose_radius``

          * **HDF5 name:** ``EncloseRadius``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`a \cdot \rm{Mpc}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - basic
     - :avail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :unavail:`SO`
     - Radius of the particle furthest from the halo centre
   * - .. dropdown:: ``maximum_circular_velocity``

          * **HDF5 name:** ``MaximumCircularVelocity``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`\rm{km} / \rm{s}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - basic
     - :avail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - Maximum circular velocity when accounting for particle softening lengths. `[3] <footnote-3_>`_
   * - .. dropdown:: ``maximum_circular_velocity_radius``

          * **HDF5 name:** ``MaximumCircularVelocityRadius``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`a \cdot \rm{Mpc}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - basic
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - Radius at which MaximumCircularVelocity is reached.
   * - .. dropdown:: ``maximum_circular_velocity_radius_unsoftened``

          * **HDF5 name:** ``MaximumCircularVelocityRadiusUnsoftened``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`a \cdot \rm{Mpc}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - basic
     - :avail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :unavail:`SO`
     - Radius at which MaximumCircularVelocityUnsoftened is reached. `[3] <footnote-3_>`_
   * - .. dropdown:: ``maximum_circular_velocity_unsoftened``

          * **HDF5 name:** ``MaximumCircularVelocityUnsoftened``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`\rm{km} / \rm{s}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - basic
     - :avail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :unavail:`SO`
     - Maximum circular velocity when not accounting for particle softening lengths. `[3] <footnote-3_>`_
   * - .. dropdown:: ``noise_suppressed_neutrino_mass``

          * **HDF5 name:** ``NoiseSuppressedNeutrinoMass``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`10^{10}\ \rm{M}_\odot`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - basic
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - Noise suppressed total neutrino mass. `[4] <footnote-4_>`_
   * - .. dropdown:: ``number_of_dark_matter_particles``

          * **HDF5 name:** ``NumberOfDarkMatterParticles``
          * **Shape:** 1
          * **Type:** uint32
          * **Units:** dimensionless
          * **Compression:** no compression
     - basic
     - :avail:`BS` :avail:`ES` :avail:`IS` :avail:`EP` :avail:`SO`
     - Number of dark matter particles.
   * - .. dropdown:: ``raw_neutrino_mass``

          * **HDF5 name:** ``RawNeutrinoMass``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`10^{10}\ \rm{M}_\odot`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - basic
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - Total neutrino particle mass. `[4] <footnote-4_>`_
   * - .. dropdown:: ``soradius``

          * **HDF5 name:** ``SORadius``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`a \cdot \rm{Mpc}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - basic
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - Radius of a sphere satisfying a spherical overdensity criterion.
   * - .. dropdown:: ``total_mass``

          * **HDF5 name:** ``TotalMass``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`10^{10}\ \rm{M}_\odot`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - basic
     - :avail:`BS` :avail:`ES` :avail:`IS` :avail:`EP` :avail:`SO`
     - Total mass.
   * - .. dropdown:: ``half_mass_radius_total``

          * **HDF5 name:** ``HalfMassRadiusTotal``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`a \cdot \rm{Mpc}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :avail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :unavail:`SO`
     - Total half mass radius. `[5] <footnote-5_>`_
   * - .. dropdown:: ``mass_fraction_external``

          * **HDF5 name:** ``MassFractionExternal``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - Fraction of mass that is bound to a satellite outside this FoF group. `[6] <footnote-6_>`_
   * - .. dropdown:: ``mass_fraction_satellites``

          * **HDF5 name:** ``MassFractionSatellites``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - Fraction of mass that is bound to a satellite in the same FoF group. `[6] <footnote-6_>`_
   * - .. dropdown:: ``spin_parameter``

          * **HDF5 name:** ``SpinParameter``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :avail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - Bullock et al. (2001) spin parameter. `[7] <footnote-7_>`_
   * - .. dropdown:: ``total_inertia_tensor``

          * **HDF5 name:** ``TotalInertiaTensor``
          * **Shape:** 6
          * **Type:** float32
          * **Units:** :math:`\rm{Mpc}^{2}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :avail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :unavail:`SO`
     - 3D inertia tensor computed iteratively from the total mass distribution, relative to the halo centre. Diagonal components and one off-diagonal triangle as (1,1), (2,2), (3,3), (1,2), (1,3), (2,3). Only calculated when we have more than 20 particles. `[8] <footnote-8_>`_
   * - .. dropdown:: ``total_inertia_tensor_noniterative``

          * **HDF5 name:** ``TotalInertiaTensorNoniterative``
          * **Shape:** 6
          * **Type:** float32
          * **Units:** :math:`\rm{Mpc}^{2}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :avail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - 3D inertia tensor computed in a single iteration from the total mass distribution, relative to the halo centre. Diagonal components and one off-diagonal triangle as (1,1), (2,2), (3,3), (1,2), (1,3), (2,3). Only calculated when we have more than 20 particles. `[8] <footnote-8_>`_
   * - .. dropdown:: ``total_inertia_tensor_reduced``

          * **HDF5 name:** ``TotalInertiaTensorReduced``
          * **Shape:** 6
          * **Type:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :avail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :unavail:`SO`
     - Reduced 3D inertia tensor computed iteratively from the total mass distribution, relative to the halo centre. Diagonal components and one off-diagonal triangle as (1,1), (2,2), (3,3), (1,2), (1,3), (2,3). Only calculated when we have more than 20 particles. `[8] <footnote-8_>`_
   * - .. dropdown:: ``total_inertia_tensor_reduced_noniterative``

          * **HDF5 name:** ``TotalInertiaTensorReducedNoniterative``
          * **Shape:** 6
          * **Type:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :avail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - Reduced 3D inertia tensor computed in a single iteration from the total mass distribution, relative to the halo centre. Diagonal components and one off-diagonal triangle as (1,1), (2,2), (3,3), (1,2), (1,3), (2,3). Only calculated when we have more than 20 particles. `[8] <footnote-8_>`_
   * - .. dropdown:: ``angular_momentum_dark_matter``

          * **HDF5 name:** ``AngularMomentumDarkMatter``
          * **Shape:** 3
          * **Type:** float32
          * **Units:** :math:`10^{10}\ \rm{Mpc} \cdot \rm{M}_\odot \cdot \rm{km} / \rm{s}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - dm
     - :avail:`BS` :avail:`ES` :avail:`IS` :unavail:`EP` :avail:`SO`
     - Total angular momentum of the dark matter, relative to the HaloCentre and DM centre of mass velocity. `[9] <footnote-9_>`_
   * - .. dropdown:: ``dark_matter_inertia_tensor``

          * **HDF5 name:** ``DarkMatterInertiaTensor``
          * **Shape:** 6
          * **Type:** float32
          * **Units:** :math:`\rm{Mpc}^{2}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - dm
     - :avail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :unavail:`SO`
     - 3D inertia tensor computed iteratively from the DM mass distribution, relative to the halo centre. Diagonal components and one off-diagonal triangle as (1,1), (2,2), (3,3), (1,2), (1,3), (2,3). Only calculated when we have more than 20 particles.
   * - .. dropdown:: ``dark_matter_inertia_tensor_noniterative``

          * **HDF5 name:** ``DarkMatterInertiaTensorNoniterative``
          * **Shape:** 6
          * **Type:** float32
          * **Units:** :math:`\rm{Mpc}^{2}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - dm
     - :avail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - 3D inertia tensor computed in a single interation from the DM mass distribution, relative to the halo centre. Diagonal components and one off-diagonal triangle as (1,1), (2,2), (3,3), (1,2), (1,3), (2,3). Only calculated when we have more than 20 particles.
   * - .. dropdown:: ``dark_matter_inertia_tensor_reduced``

          * **HDF5 name:** ``DarkMatterInertiaTensorReduced``
          * **Shape:** 6
          * **Type:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - dm
     - :avail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :unavail:`SO`
     - Reduced 3D inertia tensor computed iteratively from the DM mass distribution, relative to the halo centre. Diagonal components and one off-diagonal triangle as (1,1), (2,2), (3,3), (1,2), (1,3), (2,3). Only calculated when we have more than 20 particles.
   * - .. dropdown:: ``dark_matter_inertia_tensor_reduced_noniterative``

          * **HDF5 name:** ``DarkMatterInertiaTensorReducedNoniterative``
          * **Shape:** 6
          * **Type:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - dm
     - :avail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - Reduced 3D inertia tensor computed in a single interation from the DM mass distribution, relative to the halo centre. Diagonal components and one off-diagonal triangle as (1,1), (2,2), (3,3), (1,2), (1,3), (2,3). Only calculated when we have more than 20 particles.
   * - .. dropdown:: ``dark_matter_projected_velocity_dispersion``

          * **HDF5 name:** ``DarkMatterProjectedVelocityDispersion``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`\rm{km} / \rm{s}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - dm
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :avail:`EP` :unavail:`SO`
     - Mass-weighted velocity dispersion of the DM along the projection axis, relative to the DM centre of mass velocity. `[10] <footnote-10_>`_
   * - .. dropdown:: ``dark_matter_velocity_dispersion_matrix``

          * **HDF5 name:** ``DarkMatterVelocityDispersionMatrix``
          * **Shape:** 6
          * **Type:** float32
          * **Units:** :math:`\rm{km}^{2} / \rm{s}^{2}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - dm
     - :avail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :unavail:`SO`
     - Mass-weighted velocity dispersion of the dark matter. Measured relative to the DM centre of mass velocity. The order of the components of the dispersion tensor is XX YY ZZ XY XZ YZ. `[11] <footnote-11_>`_
   * - .. dropdown:: ``half_mass_radius_dark_matter``

          * **HDF5 name:** ``HalfMassRadiusDarkMatter``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`a \cdot \rm{Mpc}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - dm
     - :avail:`BS` :avail:`ES` :avail:`IS` :avail:`EP` :unavail:`SO`
     - Dark matter half mass radius. `[5] <footnote-5_>`_

Hydrodynamical properties
-------------------------

.. list-table::
   :widths: 25 10 15 50
   :header-rows: 1

   * - Name
     - Filter
     - Variations
     - Description
   * - .. dropdown:: ``black_holes_dynamical_mass``

          * **HDF5 name:** ``BlackHolesDynamicalMass``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`10^{10}\ \rm{M}_\odot`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - basic
     - :avail:`BS` :avail:`ES` :avail:`IS` :avail:`EP` :avail:`SO`
     - Total BH dynamical mass.
   * - .. dropdown:: ``black_holes_subgrid_mass``

          * **HDF5 name:** ``BlackHolesSubgridMass``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`10^{10}\ \rm{M}_\odot`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - basic
     - :avail:`BS` :avail:`ES` :avail:`IS` :avail:`EP` :avail:`SO`
     - Total BH subgrid mass.
   * - .. dropdown:: ``dark_matter_concentration``

          * **HDF5 name:** ``DarkMatterConcentration``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - basic
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - Concentration of dark matter particles assuming an NFW profile. Minimum particle radius set to softening length `[2] <footnote-2_>`_
   * - .. dropdown:: ``dark_matter_concentration_unsoftened``

          * **HDF5 name:** ``DarkMatterConcentrationUnsoftened``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - basic
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - Concentration of dark matter particles assuming an NFW profile. No particle softening `[2] <footnote-2_>`_
   * - .. dropdown:: ``gas_mass``

          * **HDF5 name:** ``GasMass``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`10^{10}\ \rm{M}_\odot`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - basic
     - :avail:`BS` :avail:`ES` :avail:`IS` :avail:`EP` :avail:`SO`
     - Total gas mass.
   * - .. dropdown:: ``gas_mass_fraction_in_metals``

          * **HDF5 name:** ``GasMassFractionInMetals``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - basic
     - :avail:`BS` :avail:`ES` :avail:`IS` :unavail:`EP` :avail:`SO`
     - Total gas mass fraction in metals. `[12] <footnote-12_>`_
   * - .. dropdown:: ``half_mass_radius_stars``

          * **HDF5 name:** ``HalfMassRadiusStars``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`a \cdot \rm{Mpc}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - basic
     - :avail:`BS` :avail:`ES` :avail:`IS` :avail:`EP` :unavail:`SO`
     - Stellar half mass radius. `[5] <footnote-5_>`_
   * - .. dropdown:: ``most_massive_black_hole_id``

          * **HDF5 name:** ``MostMassiveBlackHoleID``
          * **Shape:** 1
          * **Type:** uint64
          * **Units:** dimensionless
          * **Compression:** no compression
     - basic
     - :avail:`BS` :avail:`ES` :avail:`IS` :avail:`EP` :avail:`SO`
     - ID of most massive black hole.
   * - .. dropdown:: ``most_massive_black_hole_mass``

          * **HDF5 name:** ``MostMassiveBlackHoleMass``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`10^{10}\ \rm{M}_\odot`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - basic
     - :avail:`BS` :avail:`ES` :avail:`IS` :avail:`EP` :avail:`SO`
     - Mass of most massive black hole. `[13] <footnote-13_>`_
   * - .. dropdown:: ``number_of_black_hole_particles``

          * **HDF5 name:** ``NumberOfBlackHoleParticles``
          * **Shape:** 1
          * **Type:** uint32
          * **Units:** dimensionless
          * **Compression:** no compression
     - basic
     - :avail:`BS` :avail:`ES` :avail:`IS` :avail:`EP` :avail:`SO`
     - Number of black hole particles.
   * - .. dropdown:: ``number_of_gas_particles``

          * **HDF5 name:** ``NumberOfGasParticles``
          * **Shape:** 1
          * **Type:** uint32
          * **Units:** dimensionless
          * **Compression:** no compression
     - basic
     - :avail:`BS` :avail:`ES` :avail:`IS` :avail:`EP` :avail:`SO`
     - Number of gas particles.
   * - .. dropdown:: ``number_of_neutrino_particles``

          * **HDF5 name:** ``NumberOfNeutrinoParticles``
          * **Shape:** 1
          * **Type:** uint32
          * **Units:** dimensionless
          * **Compression:** no compression
     - basic
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - Number of neutrino particles.
   * - .. dropdown:: ``number_of_star_particles``

          * **HDF5 name:** ``NumberOfStarParticles``
          * **Shape:** 1
          * **Type:** uint32
          * **Units:** dimensionless
          * **Compression:** no compression
     - basic
     - :avail:`BS` :avail:`ES` :avail:`IS` :avail:`EP` :avail:`SO`
     - Number of star particles.
   * - .. dropdown:: ``star_formation_rate``

          * **HDF5 name:** ``StarFormationRate``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`10^{10}\ \frac{\rm{M}_\odot \cdot \rm{km}}{\rm{Mpc} \cdot \rm{s}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - basic
     - :avail:`BS` :avail:`ES` :avail:`IS` :avail:`EP` :avail:`SO`
     - Total star formation rate. `[14] <footnote-14_>`_
   * - .. dropdown:: ``star_forming_gas_mass_fraction_in_metals``

          * **HDF5 name:** ``StarFormingGasMassFractionInMetals``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - basic
     - :avail:`BS` :avail:`ES` :avail:`IS` :unavail:`EP` :avail:`SO`
     - Total gas mass fraction in metals for gas that is star-forming. `[12] <footnote-12_>`_ `[14] <footnote-14_>`_
   * - .. dropdown:: ``stellar_mass``

          * **HDF5 name:** ``StellarMass``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`10^{10}\ \rm{M}_\odot`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - basic
     - :avail:`BS` :avail:`ES` :avail:`IS` :avail:`EP` :avail:`SO`
     - Total stellar mass.
   * - .. dropdown:: ``stellar_mass_fraction_in_metals``

          * **HDF5 name:** ``StellarMassFractionInMetals``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - basic
     - :avail:`BS` :avail:`ES` :avail:`IS` :unavail:`EP` :avail:`SO`
     - Total stellar mass fraction in metals.
   * - .. dropdown:: ``black_holes_last_event_scalefactor``

          * **HDF5 name:** ``BlackHolesLastEventScalefactor``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :avail:`BS` :avail:`ES` :avail:`IS` :avail:`EP` :avail:`SO`
     - Scale-factor of last AGN event.
   * - .. dropdown:: ``compton_y``

          * **HDF5 name:** ``ComptonY``
          * **Shape:** 1
          * **Type:** float64
          * **Units:** :math:`\rm{Mpc}^{2}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - Total Compton y parameter. `[15] <footnote-15_>`_
   * - .. dropdown:: ``compton_ywithout_recent_agnheating``

          * **HDF5 name:** ``ComptonYWithoutRecentAGNHeating``
          * **Shape:** 1
          * **Type:** float64
          * **Units:** :math:`\rm{Mpc}^{2}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - Total Compton y parameter. Excludes gas that was recently heated by AGN. `[15] <footnote-15_>`_
   * - .. dropdown:: ``doppler_b``

          * **HDF5 name:** ``DopplerB``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`a`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - Kinetic Sunyaey-Zel'dovich effect, assuming a line of sight towards the position of the first lightcone observer. `[16] <footnote-16_>`_
   * - .. dropdown:: ``gas_compton_ytemperature``

          * **HDF5 name:** ``GasComptonYTemperature``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`\rm{K}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - ComptonY-weighted mean gas temperature. `[17] <footnote-17_>`_
   * - .. dropdown:: ``gas_compton_ytemperature_core_excision``

          * **HDF5 name:** ``GasComptonYTemperatureCoreExcision``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`\rm{K}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - ComptonY-weighted mean gas temperature, excluding the inner excised core. `[17] <footnote-17_>`_ `[18] <footnote-18_>`_
   * - .. dropdown:: ``gas_compton_ytemperature_without_recent_agnheating``

          * **HDF5 name:** ``GasComptonYTemperatureWithoutRecentAGNHeating``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`\rm{K}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - ComptonY-weighted mean gas temperature, excluding gas that was recently heated by AGN. `[17] <footnote-17_>`_
   * - .. dropdown:: ``gas_compton_ytemperature_without_recent_agnheating_core_excision``

          * **HDF5 name:** ``GasComptonYTemperatureWithoutRecentAGNHeatingCoreExcision``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`\rm{K}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - ComptonY-weighted mean gas temperature, excluding the inner excised core and gas that was recently heated by AGN. `[17] <footnote-17_>`_ `[18] <footnote-18_>`_
   * - .. dropdown:: ``gas_mass_fraction_in_iron``

          * **HDF5 name:** ``GasMassFractionInIron``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :unavail:`BS` :avail:`ES` :avail:`IS` :unavail:`EP` :avail:`SO`
     - Total gas mass fraction in iron. `[12] <footnote-12_>`_
   * - .. dropdown:: ``gas_mass_fraction_in_oxygen``

          * **HDF5 name:** ``GasMassFractionInOxygen``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :unavail:`BS` :avail:`ES` :avail:`IS` :unavail:`EP` :avail:`SO`
     - Total gas mass in oxygen. `[12] <footnote-12_>`_
   * - .. dropdown:: ``gas_temperature``

          * **HDF5 name:** ``GasTemperature``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`\rm{K}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :avail:`BS` :avail:`ES` :avail:`IS` :unavail:`EP` :avail:`SO`
     - Mass-weighted mean gas temperature. `[19] <footnote-19_>`_
   * - .. dropdown:: ``gas_temperature_core_excision``

          * **HDF5 name:** ``GasTemperatureCoreExcision``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`\rm{K}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - Mass-weighted mean gas temperature, excluding the inner excised core. `[18] <footnote-18_>`_
   * - .. dropdown:: ``gas_temperature_without_cool_gas``

          * **HDF5 name:** ``GasTemperatureWithoutCoolGas``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`\rm{K}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :avail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - Mass-weighted mean gas temperature, excluding cool gas with a temperature below 1e5 K. `[19] <footnote-19_>`_
   * - .. dropdown:: ``gas_temperature_without_cool_gas_and_recent_agnheating``

          * **HDF5 name:** ``GasTemperatureWithoutCoolGasAndRecentAGNHeating``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`\rm{K}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :avail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - Mass-weighted mean gas temperature, excluding cool gas with a temperature below 1e5 K and gas that was recently heated by AGN. `[19] <footnote-19_>`_
   * - .. dropdown:: ``gas_temperature_without_cool_gas_and_recent_agnheating_core_excision``

          * **HDF5 name:** ``GasTemperatureWithoutCoolGasAndRecentAGNHeatingCoreExcision``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`\rm{K}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - Mass-weighted mean gas temperature, excluding the inner excised core, gas below 1e5 K and gas that was recently heated by AGN. `[18] <footnote-18_>`_
   * - .. dropdown:: ``gas_temperature_without_cool_gas_core_excision``

          * **HDF5 name:** ``GasTemperatureWithoutCoolGasCoreExcision``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`\rm{K}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - Mass-weighted mean gas temperature, excluding the inner excised core and gas below 1e5 K. `[18] <footnote-18_>`_
   * - .. dropdown:: ``gas_temperature_without_recent_agnheating``

          * **HDF5 name:** ``GasTemperatureWithoutRecentAGNHeating``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`\rm{K}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :avail:`BS` :avail:`ES` :avail:`IS` :unavail:`EP` :avail:`SO`
     - Mass-weighted mean gas temperature, excluding gas that was recently heated by AGN. `[19] <footnote-19_>`_
   * - .. dropdown:: ``gas_temperature_without_recent_agnheating_core_excision``

          * **HDF5 name:** ``GasTemperatureWithoutRecentAGNHeatingCoreExcision``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`\rm{K}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - Mass-weighted mean gas temperature, excluding the inner excised core, and gas that was recently heated by AGN. `[18] <footnote-18_>`_
   * - .. dropdown:: ``hot_gas_mass``

          * **HDF5 name:** ``HotGasMass``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`10^{10}\ \rm{M}_\odot`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - Total mass of gas with a temperature above 1e5 K.
   * - .. dropdown:: ``most_massive_black_hole_accretion_rate``

          * **HDF5 name:** ``MostMassiveBlackHoleAccretionRate``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`10^{10}\ \frac{\rm{M}_\odot \cdot \rm{km}}{\rm{Mpc} \cdot \rm{s}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :avail:`BS` :avail:`ES` :avail:`IS` :avail:`EP` :avail:`SO`
     - Gas accretion rate of most massive black hole.
   * - .. dropdown:: ``most_massive_black_hole_last_event_scalefactor``

          * **HDF5 name:** ``MostMassiveBlackHoleLastEventScalefactor``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.3669{\rm{}e}10`
     - general
     - :avail:`BS` :avail:`ES` :avail:`IS` :avail:`EP` :avail:`SO`
     - Scale-factor of last thermal AGN event for most massive black hole.
   * - .. dropdown:: ``most_massive_black_hole_position``

          * **HDF5 name:** ``MostMassiveBlackHolePosition``
          * **Shape:** 3
          * **Type:** float64
          * **Units:** :math:`a \cdot \rm{Mpc}`
          * **Compression:** 1 pc accurate
     - general
     - :avail:`BS` :avail:`ES` :avail:`IS` :avail:`EP` :avail:`SO`
     - Position of most massive black hole.
   * - .. dropdown:: ``most_massive_black_hole_velocity``

          * **HDF5 name:** ``MostMassiveBlackHoleVelocity``
          * **Shape:** 3
          * **Type:** float32
          * **Units:** :math:`\rm{km} / \rm{s}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :avail:`BS` :avail:`ES` :avail:`IS` :avail:`EP` :avail:`SO`
     - Velocity of most massive black hole relative to the simulation volume.
   * - .. dropdown:: ``projected_total_inertia_tensor_noniterative``

          * **HDF5 name:** ``ProjectedTotalInertiaTensorNoniterative``
          * **Shape:** 3
          * **Type:** float32
          * **Units:** :math:`\rm{Mpc}^{2}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :avail:`EP` :unavail:`SO`
     - 2D inertia tensor computed in a single iteration from the total mass distribution, relative to the halo centre. Diagonal components and one off-diagonal value as (1,1), (2,2), (1,2). Only calculated when we have more than 20 particles. `[8] <footnote-8_>`_
   * - .. dropdown:: ``projected_total_inertia_tensor_reduced_noniterative``

          * **HDF5 name:** ``ProjectedTotalInertiaTensorReducedNoniterative``
          * **Shape:** 3
          * **Type:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :avail:`EP` :unavail:`SO`
     - Reduced 2D inertia tensor computed in a single iteration from the total mass distribution, relative to the halo centre. Diagonal components and one off-diagonal value as (1,1), (2,2), (1,2). Only calculated when we have more than 20 particles. `[8] <footnote-8_>`_
   * - .. dropdown:: ``spectroscopic_like_temperature``

          * **HDF5 name:** ``SpectroscopicLikeTemperature``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`\rm{K}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - Spectroscopic-like gas temperature. `[20] <footnote-20_>`_
   * - .. dropdown:: ``spectroscopic_like_temperature_core_excision``

          * **HDF5 name:** ``SpectroscopicLikeTemperatureCoreExcision``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`\rm{K}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - Spectroscopic-like gas temperature. Excludes gas in the inner excised core `[18] <footnote-18_>`_ `[20] <footnote-20_>`_
   * - .. dropdown:: ``spectroscopic_like_temperature_without_recent_agnheating``

          * **HDF5 name:** ``SpectroscopicLikeTemperatureWithoutRecentAGNHeating``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`\rm{K}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - Spectroscopic-like gas temperature. Exclude gas that was recently heated by AGN `[20] <footnote-20_>`_
   * - .. dropdown:: ``spectroscopic_like_temperature_without_recent_agnheating_core_excision``

          * **HDF5 name:** ``SpectroscopicLikeTemperatureWithoutRecentAGNHeatingCoreExcision``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`\rm{K}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - Spectroscopic-like gas temperature. Exclude gas that was recently heated by AGN. Excludes gas in the inner excised core `[18] <footnote-18_>`_ `[20] <footnote-20_>`_
   * - .. dropdown:: ``star_forming_gas_mass``

          * **HDF5 name:** ``StarFormingGasMass``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`10^{10}\ \rm{M}_\odot`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :avail:`BS` :avail:`ES` :avail:`IS` :unavail:`EP` :unavail:`SO`
     - Total mass of star-forming gas. `[14] <footnote-14_>`_
   * - .. dropdown:: ``star_forming_gas_mass_fraction_in_iron``

          * **HDF5 name:** ``StarFormingGasMassFractionInIron``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :unavail:`BS` :avail:`ES` :avail:`IS` :unavail:`EP` :unavail:`SO`
     - Total gas mass fraction in iron for gas that is star-forming. `[12] <footnote-12_>`_ `[14] <footnote-14_>`_
   * - .. dropdown:: ``star_forming_gas_mass_fraction_in_oxygen``

          * **HDF5 name:** ``StarFormingGasMassFractionInOxygen``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :unavail:`BS` :avail:`ES` :avail:`IS` :unavail:`EP` :unavail:`SO`
     - Total gas mass fraction in oxygen for gas that is star-forming. `[12] <footnote-12_>`_ `[14] <footnote-14_>`_
   * - .. dropdown:: ``thermal_energy_gas``

          * **HDF5 name:** ``ThermalEnergyGas``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`10^{10}\ \frac{\rm{M}_\odot \cdot \rm{km}^{2}}{\rm{s}^{2}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - Total thermal energy of the gas. `[21] <footnote-21_>`_
   * - .. dropdown:: ``xray_luminosity``

          * **HDF5 name:** ``XRayLuminosity``
          * **Shape:** 3
          * **Type:** float64
          * **Units:** :math:`10^{10}\ \frac{\rm{M}_\odot \cdot \rm{km}^{3}}{\rm{Mpc} \cdot \rm{s}^{3}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - Total observer-frame Xray luminosity in three bands. `[22] <footnote-22_>`_
   * - .. dropdown:: ``xray_luminosity_core_excision``

          * **HDF5 name:** ``XRayLuminosityCoreExcision``
          * **Shape:** 3
          * **Type:** float64
          * **Units:** :math:`10^{10}\ \frac{\rm{M}_\odot \cdot \rm{km}^{3}}{\rm{Mpc} \cdot \rm{s}^{3}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - Total observer-frame Xray luminosity in three bands. Excludes gas in the inner excised core `[18] <footnote-18_>`_
   * - .. dropdown:: ``xray_luminosity_in_restframe``

          * **HDF5 name:** ``XRayLuminosityInRestframe``
          * **Shape:** 3
          * **Type:** float64
          * **Units:** :math:`10^{10}\ \frac{\rm{M}_\odot \cdot \rm{km}^{3}}{\rm{Mpc} \cdot \rm{s}^{3}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - Total rest-frame Xray luminosity in three bands. `[22] <footnote-22_>`_
   * - .. dropdown:: ``xray_luminosity_in_restframe_core_excision``

          * **HDF5 name:** ``XRayLuminosityInRestframeCoreExcision``
          * **Shape:** 3
          * **Type:** float64
          * **Units:** :math:`10^{10}\ \frac{\rm{M}_\odot \cdot \rm{km}^{3}}{\rm{Mpc} \cdot \rm{s}^{3}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - Total rest-frame Xray luminosity in three bands. Excludes gas in the inner excised core
   * - .. dropdown:: ``xray_luminosity_in_restframe_without_recent_agnheating``

          * **HDF5 name:** ``XRayLuminosityInRestframeWithoutRecentAGNHeating``
          * **Shape:** 3
          * **Type:** float64
          * **Units:** :math:`10^{10}\ \frac{\rm{M}_\odot \cdot \rm{km}^{3}}{\rm{Mpc} \cdot \rm{s}^{3}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - Total rest-frame Xray luminosity in three bands. Excludes gas that was recently heated by AGN.
   * - .. dropdown:: ``xray_luminosity_in_restframe_without_recent_agnheating_core_excision``

          * **HDF5 name:** ``XRayLuminosityInRestframeWithoutRecentAGNHeatingCoreExcision``
          * **Shape:** 3
          * **Type:** float64
          * **Units:** :math:`10^{10}\ \frac{\rm{M}_\odot \cdot \rm{km}^{3}}{\rm{Mpc} \cdot \rm{s}^{3}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - Total rest-frame Xray luminosity in three bands. Excludes gas that was recently heated by AGN. Excludes gas in the inner excised core
   * - .. dropdown:: ``xray_luminosity_without_recent_agnheating``

          * **HDF5 name:** ``XRayLuminosityWithoutRecentAGNHeating``
          * **Shape:** 3
          * **Type:** float64
          * **Units:** :math:`10^{10}\ \frac{\rm{M}_\odot \cdot \rm{km}^{3}}{\rm{Mpc} \cdot \rm{s}^{3}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - Total observer-frame Xray luminosity in three bands. Excludes gas that was recently heated by AGN.
   * - .. dropdown:: ``xray_luminosity_without_recent_agnheating_core_excision``

          * **HDF5 name:** ``XRayLuminosityWithoutRecentAGNHeatingCoreExcision``
          * **Shape:** 3
          * **Type:** float64
          * **Units:** :math:`10^{10}\ \frac{\rm{M}_\odot \cdot \rm{km}^{3}}{\rm{Mpc} \cdot \rm{s}^{3}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - Total observer-frame Xray luminosity in three bands. Excludes gas that was recently heated by AGN. Excludes gas in the inner excised core `[18] <footnote-18_>`_
   * - .. dropdown:: ``xray_photon_luminosity``

          * **HDF5 name:** ``XRayPhotonLuminosity``
          * **Shape:** 3
          * **Type:** float64
          * **Units:** :math:`\frac{\rm{km}}{\rm{Mpc} \cdot \rm{s}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - Total observer-frame Xray photon luminosity in three bands. `[22] <footnote-22_>`_
   * - .. dropdown:: ``xray_photon_luminosity_core_excision``

          * **HDF5 name:** ``XRayPhotonLuminosityCoreExcision``
          * **Shape:** 3
          * **Type:** float64
          * **Units:** :math:`\frac{\rm{km}}{\rm{Mpc} \cdot \rm{s}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - Total observer-frame Xray photon luminosity in three bands. Excludes gas in the inner excised core `[18] <footnote-18_>`_
   * - .. dropdown:: ``xray_photon_luminosity_in_restframe``

          * **HDF5 name:** ``XRayPhotonLuminosityInRestframe``
          * **Shape:** 3
          * **Type:** float64
          * **Units:** :math:`\frac{\rm{km}}{\rm{Mpc} \cdot \rm{s}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - Total rest-frame Xray photon luminosity in three bands. `[22] <footnote-22_>`_
   * - .. dropdown:: ``xray_photon_luminosity_in_restframe_core_excision``

          * **HDF5 name:** ``XRayPhotonLuminosityInRestframeCoreExcision``
          * **Shape:** 3
          * **Type:** float64
          * **Units:** :math:`\frac{\rm{km}}{\rm{Mpc} \cdot \rm{s}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - Total rest-frame Xray photon luminosity in three bands. Excludes gas in the inner excised core
   * - .. dropdown:: ``xray_photon_luminosity_in_restframe_without_recent_agnheating``

          * **HDF5 name:** ``XRayPhotonLuminosityInRestframeWithoutRecentAGNHeating``
          * **Shape:** 3
          * **Type:** float64
          * **Units:** :math:`\frac{\rm{km}}{\rm{Mpc} \cdot \rm{s}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - Total rest-frame Xray photon luminosity in three bands. Exclude gas that was recently heated by AGN.
   * - .. dropdown:: ``xray_photon_luminosity_in_restframe_without_recent_agnheating_core_excision``

          * **HDF5 name:** ``XRayPhotonLuminosityInRestframeWithoutRecentAGNHeatingCoreExcision``
          * **Shape:** 3
          * **Type:** float64
          * **Units:** :math:`\frac{\rm{km}}{\rm{Mpc} \cdot \rm{s}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - Total rest-frame Xray photon luminosity in three bands. Exclude gas that was recently heated by AGN. Excludes gas in the inner excised core
   * - .. dropdown:: ``xray_photon_luminosity_without_recent_agnheating``

          * **HDF5 name:** ``XRayPhotonLuminosityWithoutRecentAGNHeating``
          * **Shape:** 3
          * **Type:** float64
          * **Units:** :math:`\frac{\rm{km}}{\rm{Mpc} \cdot \rm{s}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - Total observer-frame Xray photon luminosity in three bands. Exclude gas that was recently heated by AGN.
   * - .. dropdown:: ``xray_photon_luminosity_without_recent_agnheating_core_excision``

          * **HDF5 name:** ``XRayPhotonLuminosityWithoutRecentAGNHeatingCoreExcision``
          * **Shape:** 3
          * **Type:** float64
          * **Units:** :math:`\frac{\rm{km}}{\rm{Mpc} \cdot \rm{s}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - general
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - Total observer-frame Xray photon luminosity in three bands. Exclude gas that was recently heated by AGN. Excludes gas in the inner excised core `[18] <footnote-18_>`_
   * - .. dropdown:: ``angular_momentum_gas``

          * **HDF5 name:** ``AngularMomentumGas``
          * **Shape:** 3
          * **Type:** float32
          * **Units:** :math:`10^{10}\ \rm{Mpc} \cdot \rm{M}_\odot \cdot \rm{km} / \rm{s}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - gas
     - :avail:`BS` :avail:`ES` :avail:`IS` :unavail:`EP` :avail:`SO`
     - Total angular momentum of the gas, relative to the HaloCentre and gas centre of mass velocity. `[9] <footnote-9_>`_
   * - .. dropdown:: ``disc_to_total_gas_mass_fraction``

          * **HDF5 name:** ``DiscToTotalGasMassFraction``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - gas
     - :avail:`BS` :avail:`ES` :avail:`IS` :unavail:`EP` :avail:`SO`
     - Fraction of the total gas mass that is in the disc. `[23] <footnote-23_>`_
   * - .. dropdown:: ``gas_centre_of_mass``

          * **HDF5 name:** ``GasCentreOfMass``
          * **Shape:** 3
          * **Type:** float64
          * **Units:** :math:`a \cdot \rm{Mpc}`
          * **Compression:** 1 pc accurate
     - gas
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - Centre of mass of gas.
   * - .. dropdown:: ``gas_centre_of_mass_velocity``

          * **HDF5 name:** ``GasCentreOfMassVelocity``
          * **Shape:** 3
          * **Type:** float32
          * **Units:** :math:`\rm{km} / \rm{s}`
          * **Compression:** 0.1 km/s accurate
     - gas
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - Centre of mass velocity of gas.
   * - .. dropdown:: ``gas_inertia_tensor``

          * **HDF5 name:** ``GasInertiaTensor``
          * **Shape:** 6
          * **Type:** float32
          * **Units:** :math:`\rm{Mpc}^{2}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - gas
     - :avail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :unavail:`SO`
     - 3D inertia tensor computed iteratively from the gas mass distribution, relative to the halo centre. Diagonal components and one off-diagonal triangle as (1,1), (2,2), (3,3), (1,2), (1,3), (2,3). Only calculated when we have more than 20 particles.
   * - .. dropdown:: ``gas_inertia_tensor_noniterative``

          * **HDF5 name:** ``GasInertiaTensorNoniterative``
          * **Shape:** 6
          * **Type:** float32
          * **Units:** :math:`\rm{Mpc}^{2}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - gas
     - :avail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - 3D inertia tensor computed in a single iteration from the gas mass distribution, relative to the halo centre. Diagonal components and one off-diagonal triangle as (1,1), (2,2), (3,3), (1,2), (1,3), (2,3). Only calculated when we have more than 20 particles.
   * - .. dropdown:: ``gas_inertia_tensor_reduced``

          * **HDF5 name:** ``GasInertiaTensorReduced``
          * **Shape:** 6
          * **Type:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - gas
     - :avail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :unavail:`SO`
     - Reduced 3D inertia tensor computed iteratively from the gas mass distribution, relative to the halo centre. Diagonal components and one off-diagonal triangle as (1,1), (2,2), (3,3), (1,2), (1,3), (2,3). Only calculated when we have more than 20 particles.
   * - .. dropdown:: ``gas_inertia_tensor_reduced_noniterative``

          * **HDF5 name:** ``GasInertiaTensorReducedNoniterative``
          * **Shape:** 6
          * **Type:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - gas
     - :avail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - Reduced 3D inertia tensor computed in a single iteration from the gas mass distribution, relative to the halo centre. Diagonal components and one off-diagonal triangle as (1,1), (2,2), (3,3), (1,2), (1,3), (2,3). Only calculated when we have more than 20 particles.
   * - .. dropdown:: ``gas_projected_velocity_dispersion``

          * **HDF5 name:** ``GasProjectedVelocityDispersion``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`\rm{km} / \rm{s}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - gas
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :avail:`EP` :unavail:`SO`
     - Mass-weighted velocity dispersion of the gas along the projection axis, relative to the gas centre of mass velocity. `[10] <footnote-10_>`_
   * - .. dropdown:: ``gas_velocity_dispersion_matrix``

          * **HDF5 name:** ``GasVelocityDispersionMatrix``
          * **Shape:** 6
          * **Type:** float32
          * **Units:** :math:`\rm{km}^{2} / \rm{s}^{2}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - gas
     - :avail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :unavail:`SO`
     - Mass-weighted velocity dispersion of the gas. Measured relative to the gas centre of mass velocity. The order of the components of the dispersion tensor is XX YY ZZ XY XZ YZ. `[11] <footnote-11_>`_
   * - .. dropdown:: ``half_mass_radius_gas``

          * **HDF5 name:** ``HalfMassRadiusGas``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`a \cdot \rm{Mpc}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - gas
     - :avail:`BS` :avail:`ES` :avail:`IS` :avail:`EP` :unavail:`SO`
     - Gas half mass radius. `[5] <footnote-5_>`_
   * - .. dropdown:: ``kappa_corot_gas``

          * **HDF5 name:** ``KappaCorotGas``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - gas
     - :avail:`BS` :avail:`ES` :avail:`IS` :unavail:`EP` :unavail:`SO`
     - Kappa-corot for gas, relative to the HaloCentre and the centre of mass velocity of the gas. `[24] <footnote-24_>`_
   * - .. dropdown:: ``kinetic_energy_gas``

          * **HDF5 name:** ``KineticEnergyGas``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`10^{10}\ \frac{\rm{M}_\odot \cdot \rm{km}^{2}}{\rm{s}^{2}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - gas
     - :unavail:`BS` :avail:`ES` :avail:`IS` :unavail:`EP` :avail:`SO`
     - Total kinetic energy of the gas, relative to the gas centre of mass velocity. `[25] <footnote-25_>`_
   * - .. dropdown:: ``projected_gas_inertia_tensor_noniterative``

          * **HDF5 name:** ``ProjectedGasInertiaTensorNoniterative``
          * **Shape:** 3
          * **Type:** float32
          * **Units:** :math:`\rm{Mpc}^{2}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - gas
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :avail:`EP` :unavail:`SO`
     - 2D inertia tensor computed in a single iteration from the gas mass distribution, relative to the halo centre. Diagonal components and one off-diagonal value as (1,1), (2,2), (1,2). Only calculated when we have more than 20 particles.
   * - .. dropdown:: ``projected_gas_inertia_tensor_reduced_noniterative``

          * **HDF5 name:** ``ProjectedGasInertiaTensorReducedNoniterative``
          * **Shape:** 3
          * **Type:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - gas
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :avail:`EP` :unavail:`SO`
     - Reduced 2D inertia tensor computed in a single iteration from the gas mass distribution, relative to the halo centre. Diagonal components and one off-diagonal value as (1,1), (2,2), (1,2). Only calculated when we have more than 20 particles.
   * - .. dropdown:: ``maximum_dark_matter_circular_velocity``

          * **HDF5 name:** ``MaximumDarkMatterCircularVelocity``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`\rm{km} / \rm{s}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - dm
     - :avail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :unavail:`SO`
     - Maximum circular velocity calculated using dark matter particles when accounting for particle softening lengths..
   * - .. dropdown:: ``maximum_dark_matter_circular_velocity_radius``

          * **HDF5 name:** ``MaximumDarkMatterCircularVelocityRadius``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`a \cdot \rm{Mpc}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - dm
     - :avail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :unavail:`SO`
     - Radius at which MaximumDarkMatterCircularVelocity is reached.
   * - .. dropdown:: ``angular_momentum_stars``

          * **HDF5 name:** ``AngularMomentumStars``
          * **Shape:** 3
          * **Type:** float32
          * **Units:** :math:`10^{10}\ \rm{Mpc} \cdot \rm{M}_\odot \cdot \rm{km} / \rm{s}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - star
     - :avail:`BS` :avail:`ES` :avail:`IS` :unavail:`EP` :avail:`SO`
     - Total angular momentum of the stars, relative to the HaloCentre and stellar centre of mass velocity. `[9] <footnote-9_>`_
   * - .. dropdown:: ``disc_to_total_stellar_mass_fraction``

          * **HDF5 name:** ``DiscToTotalStellarMassFraction``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - star
     - :avail:`BS` :avail:`ES` :avail:`IS` :unavail:`EP` :avail:`SO`
     - Fraction of the total stellar mass that is in the disc. `[23] <footnote-23_>`_
   * - .. dropdown:: ``kappa_corot_stars``

          * **HDF5 name:** ``KappaCorotStars``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - star
     - :avail:`BS` :avail:`ES` :avail:`IS` :unavail:`EP` :unavail:`SO`
     - Kappa-corot for stars, relative to the HaloCentre and the centre of mass velocity of the stars. `[24] <footnote-24_>`_
   * - .. dropdown:: ``kinetic_energy_stars``

          * **HDF5 name:** ``KineticEnergyStars``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`10^{10}\ \frac{\rm{M}_\odot \cdot \rm{km}^{2}}{\rm{s}^{2}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - star
     - :unavail:`BS` :avail:`ES` :avail:`IS` :unavail:`EP` :avail:`SO`
     - Total kinetic energy of the stars, relative to the stellar centre of mass velocity. `[25] <footnote-25_>`_
   * - .. dropdown:: ``luminosity_weighted_mean_stellar_age``

          * **HDF5 name:** ``LuminosityWeightedMeanStellarAge``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`\rm{Mpc} \cdot \rm{s} / \rm{km}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - star
     - :avail:`BS` :avail:`ES` :avail:`IS` :unavail:`EP` :unavail:`SO`
     - Luminosity weighted mean stellar age. The weight is the r band luminosity.
   * - .. dropdown:: ``mass_weighted_mean_stellar_age``

          * **HDF5 name:** ``MassWeightedMeanStellarAge``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`\rm{Mpc} \cdot \rm{s} / \rm{km}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - star
     - :avail:`BS` :avail:`ES` :avail:`IS` :unavail:`EP` :unavail:`SO`
     - Mass weighted mean stellar age.
   * - .. dropdown:: ``projected_stellar_inertia_tensor_noniterative``

          * **HDF5 name:** ``ProjectedStellarInertiaTensorNoniterative``
          * **Shape:** 3
          * **Type:** float32
          * **Units:** :math:`\rm{Mpc}^{2}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - star
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :avail:`EP` :unavail:`SO`
     - 2D inertia tensor computed in a single iteration from the stellar mass distribution, relative to the halo centre. Diagonal components and one off-diagonal value as (1,1), (2,2), (1,2). Only calculated when we have more than 20 particles.
   * - .. dropdown:: ``projected_stellar_inertia_tensor_reduced_noniterative``

          * **HDF5 name:** ``ProjectedStellarInertiaTensorReducedNoniterative``
          * **Shape:** 3
          * **Type:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - star
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :avail:`EP` :unavail:`SO`
     - Reduced 2D inertia tensor computed in a single iteration from the stellar mass distribution, relative to the halo centre. Diagonal components and one off-diagonal value as (1,1), (2,2), (1,2). Only calculated when we have more than 20 particles.
   * - .. dropdown:: ``stellar_centre_of_mass``

          * **HDF5 name:** ``StellarCentreOfMass``
          * **Shape:** 3
          * **Type:** float64
          * **Units:** :math:`a \cdot \rm{Mpc}`
          * **Compression:** 1 pc accurate
     - star
     - :unavail:`BS` :avail:`ES` :avail:`IS` :unavail:`EP` :avail:`SO`
     - Centre of mass of stars.
   * - .. dropdown:: ``stellar_centre_of_mass_velocity``

          * **HDF5 name:** ``StellarCentreOfMassVelocity``
          * **Shape:** 3
          * **Type:** float32
          * **Units:** :math:`\rm{km} / \rm{s}`
          * **Compression:** 0.1 km/s accurate
     - star
     - :unavail:`BS` :avail:`ES` :avail:`IS` :unavail:`EP` :avail:`SO`
     - Centre of mass velocity of stars.
   * - .. dropdown:: ``stellar_inertia_tensor``

          * **HDF5 name:** ``StellarInertiaTensor``
          * **Shape:** 6
          * **Type:** float32
          * **Units:** :math:`\rm{Mpc}^{2}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - star
     - :avail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :unavail:`SO`
     - 3D inertia tensor computed iteratively from the stellar mass distribution, relative to the halo centre. Diagonal components and one off-diagonal triangle as (1,1), (2,2), (3,3), (1,2), (1,3), (2,3). Only calculated when we have more than 20 particles.
   * - .. dropdown:: ``stellar_inertia_tensor_noniterative``

          * **HDF5 name:** ``StellarInertiaTensorNoniterative``
          * **Shape:** 6
          * **Type:** float32
          * **Units:** :math:`\rm{Mpc}^{2}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - star
     - :avail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - 3D inertia tensor computed in a single iteration from the stellar mass distribution, relative to the halo centre. Diagonal components and one off-diagonal triangle as (1,1), (2,2), (3,3), (1,2), (1,3), (2,3). Only calculated when we have more than 20 particles.
   * - .. dropdown:: ``stellar_inertia_tensor_reduced``

          * **HDF5 name:** ``StellarInertiaTensorReduced``
          * **Shape:** 6
          * **Type:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - star
     - :avail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :unavail:`SO`
     - Reduced 3D inertia tensor computed iteratively from the stellar mass distribution, relative to the halo centre. Diagonal components and one off-diagonal triangle as (1,1), (2,2), (3,3), (1,2), (1,3), (2,3). Only calculated when we have more than 20 particles.
   * - .. dropdown:: ``stellar_inertia_tensor_reduced_noniterative``

          * **HDF5 name:** ``StellarInertiaTensorReducedNoniterative``
          * **Shape:** 6
          * **Type:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - star
     - :avail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :avail:`SO`
     - Reduced 3D inertia tensor computed in a single iteration from the stellar mass distribution, relative to the halo centre. Diagonal components and one off-diagonal triangle as (1,1), (2,2), (3,3), (1,2), (1,3), (2,3). Only calculated when we have more than 20 particles.
   * - .. dropdown:: ``stellar_initial_mass``

          * **HDF5 name:** ``StellarInitialMass``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`10^{10}\ \rm{M}_\odot`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - star
     - :avail:`BS` :avail:`ES` :avail:`IS` :avail:`EP` :avail:`SO`
     - Total stellar initial mass.
   * - .. dropdown:: ``stellar_luminosity``

          * **HDF5 name:** ``StellarLuminosity``
          * **Shape:** 9
          * **Type:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - star
     - :avail:`BS` :avail:`ES` :avail:`IS` :avail:`EP` :avail:`SO`
     - Total stellar luminosity in the 9 GAMA bands. `[26] <footnote-26_>`_
   * - .. dropdown:: ``stellar_mass_fraction_in_iron``

          * **HDF5 name:** ``StellarMassFractionInIron``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - star
     - :unavail:`BS` :avail:`ES` :avail:`IS` :unavail:`EP` :avail:`SO`
     - Total stellar mass fraction in iron.
   * - .. dropdown:: ``stellar_mass_fraction_in_oxygen``

          * **HDF5 name:** ``StellarMassFractionInOxygen``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - star
     - :unavail:`BS` :avail:`ES` :avail:`IS` :unavail:`EP` :avail:`SO`
     - Total stellar mass fraction in oxygen.
   * - .. dropdown:: ``stellar_projected_velocity_dispersion``

          * **HDF5 name:** ``StellarProjectedVelocityDispersion``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`\rm{km} / \rm{s}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - star
     - :unavail:`BS` :unavail:`ES` :unavail:`IS` :avail:`EP` :unavail:`SO`
     - Mass-weighted velocity dispersion of the stars along the projection axis, relative to the stellar centre of mass velocity. `[10] <footnote-10_>`_
   * - .. dropdown:: ``stellar_velocity_dispersion_matrix``

          * **HDF5 name:** ``StellarVelocityDispersionMatrix``
          * **Shape:** 6
          * **Type:** float32
          * **Units:** :math:`\rm{km}^{2} / \rm{s}^{2}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - star
     - :avail:`BS` :unavail:`ES` :unavail:`IS` :unavail:`EP` :unavail:`SO`
     - Mass-weighted velocity dispersion of the stars. Measured relative to the stellar centre of mass velocity. The order of the components of the dispersion tensor is XX YY ZZ XY XZ YZ. `[11] <footnote-11_>`_
   * - .. dropdown:: ``angular_momentum_baryons``

          * **HDF5 name:** ``AngularMomentumBaryons``
          * **Shape:** 3
          * **Type:** float32
          * **Units:** :math:`10^{10}\ \rm{Mpc} \cdot \rm{M}_\odot \cdot \rm{km} / \rm{s}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - baryon
     - :avail:`BS` :avail:`ES` :avail:`IS` :unavail:`EP` :avail:`SO`
     - Total angular momentum of baryons (gas and stars), relative to the HaloCentre and baryonic centre of mass velocity. `[9] <footnote-9_>`_
   * - .. dropdown:: ``half_mass_radius_baryons``

          * **HDF5 name:** ``HalfMassRadiusBaryons``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`a \cdot \rm{Mpc}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - baryon
     - :avail:`BS` :avail:`ES` :avail:`IS` :avail:`EP` :unavail:`SO`
     - Baryonic (gas and stars) half mass radius.
   * - .. dropdown:: ``kappa_corot_baryons``

          * **HDF5 name:** ``KappaCorotBaryons``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - baryon
     - :avail:`BS` :avail:`ES` :avail:`IS` :unavail:`EP` :unavail:`SO`
     - Kappa-corot for baryons (gas and stars), relative to the HaloCentre and the centre of mass velocity of the baryons. `[24] <footnote-24_>`_

Copied properties
-----------------

.. list-table::
   :widths: 25 10 15 50
   :header-rows: 1

   * - Name
     - Filter
     - Variations
     - Description
   * - .. dropdown:: ``input_halos_hbtplus.depth``

          * **HDF5 name:** ``InputHalos/HBTplus/Depth``
          * **Shape:** 1
          * **Type:** uint64
          * **Units:** dimensionless
          * **Compression:** no compression
     - basic
     - \-
     - Level of the subhalo in the merging hierarchy.
   * - .. dropdown:: ``input_halos_hbtplus.descendant_track_id``

          * **HDF5 name:** ``InputHalos/HBTplus/DescendantTrackId``
          * **Shape:** 1
          * **Type:** int64
          * **Units:** dimensionless
          * **Compression:** no compression
     - basic
     - \-
     - TrackId of the descendant of this subhalo. See `[27] <footnote-27_>`_
   * - .. dropdown:: ``input_halos_hbtplus.host_fofid``

          * **HDF5 name:** ``InputHalos/HBTplus/HostFOFId``
          * **Shape:** 1
          * **Type:** int64
          * **Units:** dimensionless
          * **Compression:** no compression
     - basic
     - \-
     - ID of the host FoF halo of this subhalo. Hostless halos have HostFOFId == -1
   * - .. dropdown:: ``input_halos_hbtplus.last_max_mass``

          * **HDF5 name:** ``InputHalos/HBTplus/LastMaxMass``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`10^{10}\ \rm{M}_\odot`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - basic
     - \-
     - Maximum mass of this subhalo across its evolutionary history
   * - .. dropdown:: ``input_halos_hbtplus.last_max_vmax_physical``

          * **HDF5 name:** ``InputHalos/HBTplus/LastMaxVmaxPhysical``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`\rm{km} / \rm{s}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - basic
     - \-
     - Largest value of maximum circular velocity of this subhalo across its evolutionary history
   * - .. dropdown:: ``input_halos_hbtplus.nested_parent_track_id``

          * **HDF5 name:** ``InputHalos/HBTplus/NestedParentTrackId``
          * **Shape:** 1
          * **Type:** int64
          * **Units:** dimensionless
          * **Compression:** no compression
     - basic
     - \-
     - TrackId of the parent of this subhalo.
   * - .. dropdown:: ``input_halos_hbtplus.snapshot_of_birth``

          * **HDF5 name:** ``InputHalos/HBTplus/SnapshotOfBirth``
          * **Shape:** 1
          * **Type:** int64
          * **Units:** dimensionless
          * **Compression:** no compression
     - basic
     - \-
     - Snapshot when this subhalo was formed.
   * - .. dropdown:: ``input_halos_hbtplus.snapshot_of_last_isolation``

          * **HDF5 name:** ``InputHalos/HBTplus/SnapshotOfLastIsolation``
          * **Shape:** 1
          * **Type:** int64
          * **Units:** dimensionless
          * **Compression:** no compression
     - basic
     - \-
     - Latest snapshot when this subhalo was a central. -1 if the subhalo has always been a central.
   * - .. dropdown:: ``input_halos_hbtplus.snapshot_of_last_max_mass``

          * **HDF5 name:** ``InputHalos/HBTplus/SnapshotOfLastMaxMass``
          * **Shape:** 1
          * **Type:** int64
          * **Units:** dimensionless
          * **Compression:** no compression
     - basic
     - \-
     - Latest snapshot when this subhalo had its maximum mass.
   * - .. dropdown:: ``input_halos_hbtplus.snapshot_of_last_max_vmax``

          * **HDF5 name:** ``InputHalos/HBTplus/SnapshotOfLastMaxVmax``
          * **Shape:** 1
          * **Type:** int64
          * **Units:** dimensionless
          * **Compression:** no compression
     - basic
     - \-
     - Latest snapshot when this subhalo had its largest maximum circular velocity.
   * - .. dropdown:: ``input_halos_hbtplus.track_id``

          * **HDF5 name:** ``InputHalos/HBTplus/TrackId``
          * **Shape:** 1
          * **Type:** uint64
          * **Units:** dimensionless
          * **Compression:** no compression
     - basic
     - \-
     - Unique ID for this subhalo which is consistent across snapshots.
   * - .. dropdown:: ``input_halos_fof.centres``

          * **HDF5 name:** ``InputHalos/FOF/Centres``
          * **Shape:** 3
          * **Type:** float64
          * **Units:** :math:`a \cdot \rm{Mpc}`
          * **Compression:** 1 pc accurate
     - basic
     - \-
     - Centre of mass of the host FoF halo of this subhalo. Zero for satellite and hostless subhalos.
   * - .. dropdown:: ``input_halos_fof.masses``

          * **HDF5 name:** ``InputHalos/FOF/Masses``
          * **Shape:** 1
          * **Type:** float32
          * **Units:** :math:`10^{10}\ \rm{M}_\odot`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - basic
     - \-
     - Mass of the host FoF halo of this subhalo. Zero for satellite and hostless subhalos.
   * - .. dropdown:: ``input_halos_fof.sizes``

          * **HDF5 name:** ``InputHalos/FOF/Sizes``
          * **Shape:** 1
          * **Type:** uint64
          * **Units:** dimensionless
          * **Compression:** no compression
     - basic
     - \-
     - Number of particles in the host FoF halo of this subhalo. Zero for satellite and hostless subhalos.
   * - .. dropdown:: ``soap.host_halo_index``

          * **HDF5 name:** ``SOAP/HostHaloIndex``
          * **Shape:** 1
          * **Type:** int64
          * **Units:** dimensionless
          * **Compression:** no compression
     - basic
     - \-
     - Index (within the SOAP arrays) of the top level parent of this subhalo. -1 for hostless halos.
   * - .. dropdown:: ``soap.included_in_reduced_snapshot``

          * **HDF5 name:** ``SOAP/IncludedInReducedSnapshot``
          * **Shape:** 1
          * **Type:** int32
          * **Units:** dimensionless
          * **Compression:** no compression
     - basic
     - \-
     - Whether this halo is included in the reduced snapshot.
   * - .. dropdown:: ``soap.subhalo_rank_by_bound_mass``

          * **HDF5 name:** ``SOAP/SubhaloRankByBoundMass``
          * **Shape:** 1
          * **Type:** int32
          * **Units:** dimensionless
          * **Compression:** no compression
     - basic
     - \-
     - Ranking by mass of the halo within its parent field halo. Zero for the most massive halo in the field halo.

Footnotes
---------

.. _footnote-1:

**[1]** **The centre of mass and centre of mass velocity** are computed using all
particle types except neutrinos.

.. _footnote-2:

**[2]** **The concentration** is computed using the
method described in `Wang et al. (2024) <https://ui.adsabs.harvard.edu/abs/2024MNRAS.52710760W>`_, but using a fifth order polynomial fit to
the R1-concentration relation for :math:`1<c<1000`. Therefore, we set a floor of 1 and
a ceiling of 1000 for the values calculated by SOAP. This method assumes halos have
an NFW profile, and is only calculated for the
following SO variations: 200 crit, 200 mean, and BN98.
Neutrinos are included in the calculation of total concentration.
The first moment of the density distribution, :math:`R1`, can be estimated from
the concentration. From :math:`R1` the Einasto concentration can be calculated. It
also possible to estimate other properties, such as :math:`v_{max}`, by using the :math:`R1`
value and assuming an NFW profile.

.. _footnote-3:

**[3]** **The maximum circular velocity and the radius where it is reached** are
computed using

.. math::

   v_{\rm{}max} = \sqrt{\frac{G M(\leq{}r)}{r}},

where the cumulative mass :math:`M(r)` includes all particles within the radius :math:`r`, and includes the
contribution of the particle(s) at :math:`r=0`. The radius is computed relative to the halo centre.
The softened :math:`v_{max}` value is calculated using the same method, except that the particle
radius has a floor equal to the softening length. An alternative way to calculate :math:`v_{max}`
is to estimate it from the halo concentration by assuming an NFW profile. We store the radius of the
unsoftened maximum circular velocity. If the softened and unsoftened maximum circular velocities are
equal, then their radii will also be equal. If the values are not equal, then the radius of the
softened maximum circular velocity will be the simulation softening length.
Note that the softened vmax is :math:`*not*` the :math:`v_{max}` computed using a softened potential.

.. _footnote-4:

**[4]** **The neutrino masses** exist in two flavours. ``RawNeutrinoMass`` is
obtained by simply summing the neutrino particle masses, while the noise suppressed version, 
``NoiseSuppressedNeutrinoMass`` is defined as

.. math::

   M_{\nu{},{\rm{}NS}} = \sum_i m_i w_i + \frac{4\pi{}}{3} \rho{}_{\nu{}} R_{\rm{}SO}^3,

where :math:`w_i` are the neutrino weights (which can be negative), and :math:`_{}` is the background density 
of neutrinos that is also used in the SO radius calculation. The latter is obtained from the snapshot header.

.. _footnote-5:

**[5]** **The half mass radius** is determined by linear interpolation of the
cumulative mass profile obtained after sorting all particles by radius. For the projected apertures, SOAP 
uses the 2D radius (distance to the projection axis) instead of the 3D radius.

.. _footnote-6:

**[6]** **The satellite mass fractions** is obtained by summing the masses of all
particles within the inclusive sphere that are bound to a subhalo that is not the central subhalo, and 
dividing this by :math:`M_{SO}`. This uses the same membership information as is used to decide what 
particles need to be included in the exclusive sphere and projected aperture properties. For MassFractionSatellites
we only consider particles with the same FoF ID as the most bound particle in the central subhalo. For
MassFractionExternal we include all particles with a FoF ID not equal to the most bound particle in the central subhalo.

.. _footnote-7:

**[7]** **The spin parameter** is computed following `Bullock et al. (2001) <https://ui.adsabs.harvard.edu/abs/2001ApJ...555..240B>`_:

.. math::

   \lambda{} = \frac{|\vec{L}_{\rm{}tot}|}{\sqrt{2}M v_{\rm{}max} R},

where :math:`L_{tot}` is the total angular momentum of all particles within radius :math:`R`, and :math:`M` their 
total mass. The angular momentum is computed relative to the halo centre and the total centre of mass 
velocity. Since subhalos do not have a natural radius associated with them, we use the radius where the softened
:math:`v_{max}` is reached.

.. _footnote-8:

**[8]** **The inertia tensor** for a set of particles is computed as

.. math::

   I_{ij} = \frac{1}{\sum_k m_k} \sum_k m_k \; r_{k,i} \; r_{k, j}

where the index :math:`k` loops over all particles, :math:`m_k` is the mass of particle :math:`k`, and :math:`r_{k, i}` is the :math:`i`-component of the position vector of particle :math:`k` relative to the halo centre. We first compute the inertia tensor using all particles within a sphere (with radius equal to the aperture size, except for subhalos where we use the half mass radius of the particles). This is the tensor we output in the non-iterative case. In the iterative case we construct an ellipsoid with a volume equal to the initial sphere, but whose shape is given by the inertia tensor. We then recalculate the inertia tensor using only the particles within the ellipsoid. This process is repeated until the value of the :math:`q` parameter converges, or we reach 20 iterations. If at any point during the iterations there is only a single particle within the ellipsoid, we return zero. For projected apertures the process is similar, except we use circles and ellipses in the projected plane to determine which particles to include.

The reduced inertia tensor is calculated as

.. math::

   I_{ij} = \frac{1}{\sum_k m_k} \sum_k m_k \; r_{k,i} \; r_{k, j} \; r_{k}^{-2}

where :math:`r_k` is the radial distance of the particle.

We do not calculate the inertia tensor if there are fewer than 20 particles within the initial sphere.

When calculating the inertia tensor for a bound subhalo we use a sphere with a radius equal to the half mass radius of the particles being considered.

.. _footnote-9:

**[9]** **The angular momentum** of gas, dark matter, or stars is computed relative to
the halo centre and the centre of mass velocity of that particular component, and not to the 
total centre of mass velocity. The full expression is

.. math::

   \vec{L}_{\rm{}comp} = \sum_{i={\rm{}comp}} m_i \left(\vec{x}_{r,i} \times{} \vec{v}_{{\rm{}comp},r,i} \right),

with the sum :math:`i` over all particles of that particular component (bound to the halo), and

.. math::

   \vec{x}_{r,i} = \vec{x}_i - \vec{x}_{\rm{}cop},

.. math::

   \vec{v}_{{\rm{}comp},r,i} = \vec{v}_i - \vec{v}_{\rm{}com,comp},

where

.. math::

   \vec{v}_{\rm{}com,comp} = \frac{\sum_{i={\rm{}comp}} m_i \vec{v}_i}{\sum_{i={\rm{}comp}} m_i}.

We also compute the angular momentum for baryons, where the sum is then over both gas and star 
particles.

.. _footnote-10:

**[10]** **The projected velocity dispersion** is computed along the projection axis.
Along this axis the velocity is a 1D quantity, so the velocity dispersion is simply a scalar.

.. _footnote-11:

**[11]** **The velocity dispersion matrix** is defined as

.. math::

   V_{\rm{}disp,comp} = \frac{1}{\sum_{i={\rm{}comp}} m_i} \sum_{i={\rm{}comp}} m_i \vec{v}_{{\rm{}comp},r,i}\vec{v}_{{\rm{}comp},r,i},

where we compute the relative velocity as before, i.e. w.r.t. the centre of mass velocity of the particular 
component of interest. While it is strictly speaking a :math:`3  3` matrix, there are only 6 independent 
components. We use the following convention to output those 6 components as a 6-element array:

.. math::

   V'_{\rm{}disp} = \begin{pmatrix}
       V_{xx} & V_{yy} & V_{zz} & V_{xy} & V_{xz} & V_{yz}
       \end{pmatrix}.

Other velocity dispersion definitions can be derived from this general form. The one-dimensional velocity dispersion can be calculated as

.. math::

   \sigma = \sqrt{\frac{V_{xx} + V_{yy} + V_{zz}}{3}}

.. _footnote-12:

**[12]** **The oxygen and iron masses** are computed from
``SmoothedElementMassFractions`` and not ``ElementMassFractions``, since the latter were not output in 
the FLAMINGO snapshots. Metal mass fractions on the other hand are based on ``MetalMassFractions``.

.. _footnote-13:

**[13]** **The most massive black hole** is identified based using subgrid masses of the black holes.

.. _footnote-14:

**[14]** **When distinguishing between star-forming and non star-forming gas and computing the total star formation rate,** we have to be careful about the interpretation of the
``StarFormationRates`` dataset in the snapshots, since negative values in that dataset are used to store 
another quantity, the last scale factor when that particular gas particle was star-forming. Star-forming gas 
is then gas for which ``StarFormationRates`` is strictly positive, and the total star formation rate is the 
sum of only the strictly positive values.

.. _footnote-15:

**[15]** **The Compton y parameter** is computed as in `McCarthy et al. (2017) <https://ui.adsabs.harvard.edu/abs/2017MNRAS.465.2936M>`_:

.. math::

   y \, {d_A}^2(z) = \sum_i \frac{\sigma{}_T}{m_e c^2} n_{e,i} k_B T_{e,i} V_i,

where :math:`d_A(z)` is the angular diameter distance, :math:`_T` is the Thomson cross section, :math:`m_e` the electron mass, :math:`c` the speed of light and :math:`k_B` the 
Boltzmann constant. :math:`n_{e,i}` and :math:`T_{e,i}` are the electron number density and electron temperature for gas 
particle :math:`i`, while :math:`V_i=m_i/_i` is the SPH volume element that turns the sum over all particles :math:`i` 
within the inclusive sphere into a volume integral. Note that the snapshot already contains the individual 
:math:`y_i` values for the SPH particles.

.. _footnote-16:

**[16]** **The Doppler B parameter** is computed as in `Roncarelli et al. (2018) <https://ui.adsabs.harvard.edu/abs/2017MNRAS.467..985R>`_:

.. math::

   b = \frac{\sigma{}_T}{c} \sum_i n_{e,i} v_{r,{\rm{}obs},i} \frac{m_i}{\rho{}_i A_{\rm{}obs}},

where :math:`_T` is the Thomson cross section, :math:`c` the speed of light, :math:`n_{e,i}` the electron number density 
for gas particle :math:`i`, with :math:`V_i=m_i/_i` the corresponding SPH particle volume. The relative 
*peculiar* velocity is taken relative to the box and along a line of sight towards a particular observer, 
so

.. math::

   v_{r,{\rm{}obs},i} = \vec{v}_{i} \cdot{}
         \frac{\left(\vec{x}_i - \vec{x}_{\rm{}obs}\right)}{\left|\vec{x}_i - \vec{x}_{\rm{}obs}\right|},

with :math:`x_i` and :math:`v_i` the physical position and velocity of particle :math:`i`, and :math:`x_{obs}` 
the arbitrary observer position.

The surface area :math:`A_{obs}` that turns the volume integral into a line integral is that of the aperture 
for which :math:`b` is computed, i.e. :math:`A_{obs}= R_{SO}^2`.

As the observer position we use the position of the observer for the first lightcone in the simulation, or the 
centre of the box if no lightcone was present. This choice is arbitrary and can be adapted. Since 
:math:`x_{obs}` can in principle coincide with :math:`x_i`, we make sure :math:`v_{r,{obs},i}` is set to 
zero in this case to avoid division by zero.

.. _footnote-17:

**[17]** **The Compton Y-weighted temperature** is computed as

.. math::

   T = \frac{1}{\sum_i y_i} \sum_i y_i T_i,

.. _footnote-18:

**[18]** **Core excised quantities** exclude the inner region of the halo when computing the quantity.
They are only calculated for 500 crit. Any core excised calculation only uses the particles
for which

.. math::

   0.15 R_{500c} \leq \mathbf{r} \leq R_{500c}

.. _footnote-19:

**[19]** **The mass-weighted temperature** is computed as

.. math::

   T = \frac{1}{\sum_i m_i} \sum_i m_i T_i,

and the ``GasTemperatureWithoutRecentAGNHeating`` variant uses the same definition, but excludes particles 
that satisfy

.. math::

   0.1 \Delta{}T_{\rm{}AGN} \leq{} T_i \leq{} 10^{0.3} \Delta{}T_{\rm{}AGN},

and

.. math::

   \verb+LastAGNFeedbackScaleFactors+_i \geq{} a(t - 15{\rm{}Myr})

where :math:` T_{AGN}` is the same value as used internally by SWIFT, :math:`t` is the cosmic time, and :math:`a()` 
gives the scale factor as a function of time.

.. _footnote-20:

**[20]** **The spectroscopic-like temperature** is computed as

.. math::

   T_{SL} = \frac{\sum_i \rho_i m_i T_i^{1/4}}{\sum_i \rho_i m_i T_i^{-3/4}}

.. _footnote-21:

**[21]** **The thermal energy** of the gas is computed from the density and pressure,
since the internal energy was not output in the FLAMINGO snapshots. The relevant equation is

.. math::

   u = \frac{P}{(\gamma{}-1)\rho{}},

with :math:`=5/3`.

.. _footnote-22:

**[22]** **X-ray quantities are** computed directly from the X-ray datasets in the
snapshot. They are either in the emission rest-frame, or in the observed-frame of a :math:`z=0` observer, using
the redshift of the snapshot as the emission redshift . The three bands are always given in the same 
order as in the snapshot:

#. eROSITA low/soft (:math:`0.2-2.3` keV)
#. eROSITA high/hard (:math:`2.3-8` keV)
#. ROSAT (:math:`0.5-2` keV)

.. _footnote-23:

**[23]** **DiscToTotal fractions** are computed as

.. math::

   D/T = 1 - \frac{2 M_{\rm{}corot}}{M_{\rm{}Tot}},

where :math:`M_{corot}` is the sum of the mass of the counter-rotating particles,
and :math:`M_{Tot}` is the total mass of particles. This can lead to negative values,
e.g. if there are a small number of particles moving quickly in one direction, and
a larger number of particles moving slowly in the opposite direction. In this case
the larger number of particles could be marked as counter-rotating since the net
angular momentum is dominated by the small number of rapidly rotating particles.

.. _footnote-24:

**[24]** **Kappa-corot** is computed as in `Correa et al. (2017) <https://ui.adsabs.harvard.edu/abs/2017MNRAS.472L..45C>`_:

.. math::

   \kappa_{\rm{}corot,comp} = \frac{K_{\rm{}corot,comp}}{K_{\rm{}comp}},

with the kinetic energy given by

.. math::

   K_{\rm{}comp} = \frac{1}{2} \sum_{i={\rm{}comp}} m_i |\vec{v}_{{\rm{}comp},r,i}|^2,

the corotational kinetic energy given by

.. math::

   K_{\rm{}corot,comp} = \sum_{i={\rm{}comp}} \begin{cases}
       K_{{\rm{}rot,comp},i}, &L_{{\rm{}comp},p,i} > 0, \\
       0, &L_{{\rm{}comp},p,i} \leq{} 0, \\
       \end{cases}

the corotational kinetic energy given by

.. math::

   K_{\rm{}corot,comp} = \sum_{i={\rm{}comp}} \begin{cases}
       K_{{\rm{}rot,comp},i}, &L_{{\rm{}comp},p,i} > 0, \\
       0, &L_{{\rm{}comp},p,i} \leq{} 0, \\
       \end{cases}

the rotational kinetic energy given by

.. math::

   K_{{\rm{}rot,comp},i} = \frac{1}{2} \frac{L_{{\rm{}comp},p,i}^2}{m_i R_i^2},

the projected angular momentum along the angular momentum direction given by

.. math::

   L_{{\rm{}comp},p,i} = \vec{L}_i \frac{\vec{L}_{\rm{}comp}}{|\vec{L}_{\rm{}comp}|},

and the orthogonal distance to the angular momentum vector given by

.. math::

   R_i^2 = |\vec{x}_{r,i}|^2 - \left(\vec{x}_{r,i} \frac{\vec{L}_{\rm{}comp}}{|\vec{L}_{\rm{}comp}|}\right)^2,

where the angular momentum vector and the relative position and velocity are the same as above for 
consistency.

.. _footnote-25:

**[25]** **The kinetic energy** is computed using the velocities relative to the centre of mass velocity of all the particles in the aperture. The Hubble flow is included when computing the velocities.

.. _footnote-26:

**[26]** **Luminosities are given in the GAMA bands** and always using the same order
as in the snapshots: u, g, r, i, z, Y, J, H, K. These are rest-frame dust-free
AB-luminosities of the star particles. These were computed using the `Bruzual \& Charlot 2003 <https://ui.adsabs.harvard.edu/abs/2003MNRAS.344.1000B>`_
(GALAXEV) models convolved with different filter bands and interpolated in
log-log (f(log(Z), log(age)) = log(flux)) as used in the dust-free modelling
of Trayford et al. (2015). The luminosities are given in dimensionless
units. They have been divided by 3631 Jy already, i.e. they can be turned
into absolute AB-magnitudes (rest-frame absolute maggies) directly by
applying -2.5 log10(L) without additional corrections.

.. _footnote-27:

**[27]** HBT only assigns the DescendantTrackId value at the snapshot when a subhalo becomes an orphan. However, the SOAP catalogues only contain subhalos which are
resolved at the current snapshot. Therefore in order to get the descendant of a disrupted object the HBT catalogues must be used.

