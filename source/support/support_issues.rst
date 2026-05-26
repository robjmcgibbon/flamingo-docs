Known issues
============

This page tracks known technical issues related to the data products.
It will be updated as new issues are discovered.

.. contents::
   :local:
   :backlinks: none

Simulation
----------

.. _issues_bh_satellites:

Black holes in satellite galaxies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For computational efficiency reasons, black hole particles are only repositioned (i.e. moved by hand down the potential gradient to compensate for unresolved dynamical friction) onto gas particles. For gas-poor galaxies, such as low-mass satellites, this can have the consequence that black holes leave their host galaxy, either temporarily or permanently. Care should therefore be taken when studying black holes and/or AGN feedback in satellite galaxies. See also :ref:`issues_lightcone_satellites`.

.. _issues_sf_threshold:

Star formation metallicity threshold
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In all intermediate-resolution simulations except for the Jet models, particles with metallicity equal to precisely zero used a star formation threshold density of :math:`n_\text{H} = 10~\text{cm}^{-3}` instead of  :math:`10^{-1}~\text{cm}^{-3}`. Tests show that this only has significant effects on galaxies with fewer than 10 star particles, where it artificially suppresses the stellar-to-halo mass ratio.

.. _issues_agn_heating:

AGN heating
~~~~~~~~~~~

AGN feedback is implemented by heating/kicking particles to very high temperatures/velocities,
which is necessary to overcome numerical overcooling. Because the gas particles subject to energy injection by feedback are selected from the
SPH neighbours of black holes/young stars, they tend to be
part of the dense interstellar medium. This implies that for
a few time steps following energy injection, i.e. until the
particles have responded hydrodynamically to the energy
injection, such dense and hot gas can artificially distort the
observational properties of galaxies, such as their X-ray
emission. We therefore advise to test the effect of excluding recently heated/kicked particles, which can be done
using the particle property tracking the last time a particle was injected with AGN feedback energy. For some
observables (Gas and Spectroscopic-like temperatures, ComptonY properties, X-ray
properties) the SOAP catalogues provide versions that exclude particles that were subject to direct AGN heating
in the last 15 Myr and whose temperatures are between
:math:`10^{-1}\Delta T_\text{AGN}` and :math:`10^{0.3}\Delta T_\text{AGN}`, where :math:`\Delta T_\text{AGN}` is the AGN heating temperature
(but see also :ref:`Incorrect ΔT for filtering recently heated gas<issues_incorrect_dT>`).

Snapshots
---------

.. _issues_dmantissa:

HDF5 erroneously flags datasets as being corrupted
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Starting with HDF5 version 1.14.4, datasets with a :ref:`compression filter
<faq_compression>` which compresses the data by more than 2x are flagged as problematic.
This affects the following fields in the snapshots ``PartType0/MaximalTemperatures``, ``PartType0/ElectronNumberDensities``. The h5py python package does not currently support the option to disable this flag, so a version built with ``HDF5 < 1.14.4`` must be used.

Halo catalogues
---------------

.. _issues_hbt_hubble:

Incorrect value of H(z) used by HBT-HERONS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For a small number of snapshots HBT-HERONS used the value :math:`H(z) / h` instead of :math:`H(z)`.
This incorrect value is expected to have a negligible effect, as it is only used during the unbinding step.
.. since we add the Hubble flow to particles when calculating their kinetic energy.
The snapshots affected are:

 * Jet: snapshot 74
 * Jet_fgas-4σ: snapshot 76
 * M*−σ_fgas−4σ: snapshot 61
 * L2p8_m9: snapshots 26,46,63

.. _issues_missing_hbt:

Missing HBT-HERONS catalogues
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The full set of SOAP catalogues is available for the L1_m10, but the original HBT-HERONS catalogues have been lost. This means it is not possible to reconstruct the full merger tree for this run.

.. _issues_fof_centres:

FoF centres stored with extra scale factor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The values in the dataset ``soap.input_halos_fof.centres`` should be multiplied by :math:`1/a`.

.. _issues_incorrect_dT:

Incorrect :math:`\Delta T_\text{AGN}` for filtering recently heated gas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As described in :ref:`issues_agn_heating`, for a number of properties we filter out particles which have been recently
heated by AGN feedback. The :math:`\Delta T_\text{AGN}` value from the L1_m9 simulation was used for all SOAP catalogues, rather
than the :math:`\Delta T_\text{AGN}` value from the corresponding run (see Table 1 of `Schaye et al. (2023)
<https://ui.adsabs.harvard.edu/abs/2023MNRAS.tmp.2384S>`__). No filtering was done for gas particles in the Jet runs.
The impact of this on scaling relations :ref:`can be found here<issues_incorrect_dT_images>`.

.. _issues_unsoftened_spin:

Unsoftened Vmax used for spin parameter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We store the ``MaximumCircularVelocity`` calculated using both softened and unsoftened particle positions.
The unsoftened values of ``MaximumCircularVelocity`` can be unphysically large in some
instances. For most runs the softened value was correctly used to calculate ``BoundSubhalo/SpinParameter``, but for the following runs the unsoftened value
was used:

  * PlanckNu0p24Var: all snapshots except 77
  * PlanckNu0p24Fix: all snapshots except 77
  * PlanckNu0p48Fix: all snapshots except 77
  * fgas+2σ: all snapshots except 77
  * fgas−2σ: all snapshots except 77
  * fgas−4σ: snapshots 37-58
  * fgas−8σ: snapshots 37-65
  * L5p6_m10_DMO: all snapshots

.. _issues_skip_large:

Large physical apertures skipped for high redshift
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SOAP computes Inclusive and Exclusive spheres using a fixed physical aperture for every subhalo.
At high redshifts this corresponds to a very large comoving volume, and so the largest physical apertures were not computed
for redshifts greater than 3 for the L1m8 run.

.. _issues_missing_tensors:

Missing inertia tensors
~~~~~~~~~~~~~~~~~~~~~~~

When computing the inertia tensors, a filter was applied based on subhalo bound mass (:math:`2 \times 10^{11} \mathrm{M_\odot}`),
instead of the normal particle number threshold.
This means the tensors are not available for low mass subhaloes.

Halo lightcones
---------------

.. _issues_lightcone_satellites:

Missing satellite galaxies
~~~~~~~~~~~~~~~~~~~~~~~~~~

Related to :ref:`issues_bh_satellites`. We use the locations of black hole particles to place galaxies on the lightcone.
Since some galaxies have no black holes, this means a fraction of them are missing from the galaxy lightcones.
This is particularly relevant for poorly resolved galaxies, and is more important for satellites than for centrals.
Figures showing the fraction of haloes which are affected at redshift :math:`z=0` :ref:`can be found here<issues_lightcone_satellites_images>`.

HEALpix maps
------------

.. _issues_dispersion_measure:

Dispersion measure and kinetic SZ correction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The original HEALPix maps for the kinetic SZ effect
and the dispersion measure were computed using an incorrect
power of the cosmological scale factor. This was corrected using the expansion factor of the midpoint of each
lightcone shell, which has a width of ∆z = 0.05. Note
that for those simulations and redshifts for which particle
lightcone data is available, the maps can be recomputed if
desired.

.. _issues_unweighted_neutrino:

Unweighted neutrino masses used for maps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Unweighted neutrino masses were used to generate the maps, which means the maps are noisier than they could have been.

.. _issues_map_smoothing:

Incorrect search radius for smoothing particles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When constructing the FLAMINGO smoothed maps, a given particle property is either added to a singular pixel
or smoothed over multiple pixels provided its search radius, :math:`\theta_{\mathrm{s}}`, is greater than the radius of a pixel in the map,
as described in Appendix A2 of `Schaye et al. (2023)
<https://ui.adsabs.harvard.edu/abs/2023MNRAS.tmp.2384S>`__. The search radius is proportional to the particle's sph smoothing length, :math:`h`,
when projected onto the sky, :math:`\theta_{\mathrm{s}} \propto \arctan(h/r)`, where :math:`r` is the co-moving distance from the observer to the particle.
The on-the-fly HEALPix maps erroneously used a search radius that was to small by a factor of :math:`\approx 1.9` when determining if a particle should be
smoothed onto the map. Hence, particles with an angular smoothing length 1-1.9 times the pixel radii were not smoothed and instead only updated a
singular pixel. Particles with a larger or smaller angular smoothing length were treated correctly.
Furthermore, this bug only affected whether a particle should be smoothed; it had no impact on identifying pixels within
the search radius to update or on the actual smoothing of the particle's value across the smoothing kernel. `McDonald et al. (2026)
<https://ui.adsabs.harvard.edu/abs/2026arXiv260202484M>`__ finds that this bug has a negligible effect on cross-correlations computed with the smoothed X-ray maps.

.. All maps except xray, also xray maps above z=0.5 for L1 runs, xray maps for all cosmology runs

.. _issues_bright_pixels:

Unusually bright X-ray pixels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A very small number of pixels in the X-ray HEALPix maps are unusually bright compared to all other pixels within that same lightcone shell (i.e. across all HEALPix maps at a given redshift) and constitute a significant portion of each map's total X-ray emission (up to 35% in some cases). For each lightcone shell we class a pixel as being 'unusually' bright if: 1) the same pixel is the most X-ray bright in each X-ray map at a given redshift, 2) this pixel is atleast two orders of magnitude brighter than the next brightest pixel in a given X-ray map and 3) each of the neighouring pixels. Note these criteria only apply to the nside 16384 HEALPix maps. These pixels could not be reproduced from the particle lightcones.

.. note:: The recomputed X-ray maps (datasets with a ``_Recomp`` suffix in the ``lightcone*.hdf5`` files) are not affected.

Affected maps and pixels:

   * ``Planck``:
      * Observer 1, shell 1
         * `/FLAMINGO/L1_m9/Planck/healpix_maps/nside_16384/lightcone1_shells/shell_1/ </flamingo/viewer.html?path=/FLAMINGO/L1_m9/Planck/healpix_maps/nside_16384/lightcone1_shells/shell_1/>`__
         * pixel index 924361336

   * ``L2p8_m9``:
      * Observer 0, shell 55
         * `/FLAMINGO/L2p8_m9/L2p8_m9/healpix_maps/nside_16384/lightcone0_shells/shell_55/ </flamingo/viewer.html?path=/FLAMINGO/L2p8_m9/L2p8_m9/healpix_maps/nside_16384/lightcone0_shells/shell_55/>`__
         * pixel index 2857106781
      * Observer 3, shell 1
         * `/FLAMINGO/L2p8_m9/L2p8_m9/healpix_maps/nside_16384/lightcone3_shells/shell_1/ </flamingo/viewer.html?path=/FLAMINGO/L2p8_m9/L2p8_m9/healpix_maps/nside_16384/lightcone3_shells/shell_1/>`__
         * pixel index 2440147541

   * ``LS8``:
      * Observer 0, shell 14
         * `/FLAMINGO/L1_m9/LS8/healpix_maps/nside_16384/lightcone0_shells/shell_14/ </flamingo/viewer.html?path=/FLAMINGO/L1_m9/LS8/healpix_maps/nside_16384/lightcone0_shells/shell_14/>`__
         * pixel index 2619121853

   * ``PlanckDCDM12``:
      * Observer 1, shell 9
         * `/FLAMINGO/L1_m9/PlanckDCDM12/healpix_maps/nside_16384/lightcone1_shells/shell_9/ </flamingo/viewer.html?path=/FLAMINGO/L1_m9/PlanckDCDM12/healpix_maps/nside_16384/lightcone1_shells/shell_9/>`__
         * pixel index 1915507559

   * ``PlanckNu0p24Fix``:
      * Observer 0, shell 3
         * `/FLAMINGO/L1_m9/PlanckNu0p24Fix/healpix_maps/nside_16384/lightcone0_shells/shell_3/ </flamingo/viewer.html?path=/FLAMINGO/L1_m9/PlanckNu0p24Fix/healpix_maps/nside_16384/lightcone0_shells/shell_3/>`__
         * pixel index 2809245861

   * ``PlanckNu0p24Var``:
      * Observer 0, shell 8
         * `/FLAMINGO/L1_m9/PlanckNu0p24Var/healpix_maps/nside_16384/lightcone0_shells/shell_8/ </flamingo/viewer.html?path=/FLAMINGO/L1_m9/PlanckNu0p24Var/healpix_maps/nside_16384/lightcone0_shells/shell_8/>`__
         * pixel index 2953084165

   * ``Mstar-1sigma``:
      * Observer 0, shell 22
         * `/FLAMINGO/L1_m9/Mstar-1sigma/healpix_maps/nside_16384/lightcone0_shells/shell_22/ </flamingo/viewer.html?path=/FLAMINGO/L1_m9/Mstar-1sigma/healpix_maps/nside_16384/lightcone0_shells/shell_22/>`__
         * pixel index 2289480478

   * ``fgas-4sigma``:
      * Observer 0, shell 38
         * `/FLAMINGO/L1_m9/fgas-4sigma/healpix_maps/nside_16384/lightcone0_shells/shell_38/ </flamingo/viewer.html?path=/FLAMINGO/L1_m9/fgas-4sigma/healpix_maps/nside_16384/lightcone0_shells/shell_38/>`__
         * pixel index 1154659568
      * Observer 1, shell 2
         * `/FLAMINGO/L1_m9/fgas-4sigma/healpix_maps/nside_16384/lightcone1_shells/shell_2/ </flamingo/viewer.html?path=/FLAMINGO/L1_m9/fgas-4sigma/healpix_maps/nside_16384/lightcone1_shells/shell_2/>`__
         * pixel index 1219684110

.. _issues_xray_uvb:

Incorrect UVB used for computing X-ray values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The X-ray tables used to compute X-ray luminosities when running the simulations assumed the z=0 UV background for all redshifts. The X-ray values have been recomputed for
all the snapshots using a corrected table. We have also recomputed the X-ray maps where possible, but the shells above :math:`z=0.5` for the
:math:`1 \mathrm{Gpc}` runs have not been corrected.
Note that the tables used to compute the radiative cooling rates that are used during the simulation did use the correct, evolving UV background.

Particle lightcones
-------------------

.. _issues_reposition_bh:

Replication of black holes
~~~~~~~~~~~~~~~~~~~~~~~~~~

The repositioning of a black hole particle can cause it to cross into the lightcone.
When this happens, the same black hole can appear in the lightcone outputs multiple times in quick succession.
Similarly repositioning a black hole out of the lightcone can cause it to be to be missing.
Note that it is expected that individual particles appear in the lightcone multiple times due to box replication,
but they should not do so in very close succession. This affects the lightcones for all runs, but the effect
is negligible (it occurs approximately once for every ten thousand times a black hole appears in the lightcone).
A figure showing the distribution of the distance between replicated particles :ref:`can be found here<issues_reposition_bh_images>`.

.. _issues_compression:

Compression of scale factors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A ``Bfloat16`` :ref:`lossy compression filter<faq_compression>` was applied to the dataset ``PartType0/LastAGNFeedbackScaleFactors``
in the particle lightcones.
The reduced precision means it is not possible to reliably determine whether a particle was heated by an AGN within the last 15 Myr (as discussed in :ref:`issues_agn_heating`).
A figure which gives a full description of this issue :ref:`can be found here<issues_compression_images>`.
A alternative cut is to apply a time limit of 70 Myr, a density cut of :math:`\rho_{\mathrm{gas}}~ > 10^{-26} \mathrm{g~cm}^{-3}`, and the standard temperature constraint (:math:`10^{-1} \Delta T_{\mathrm{AGN}} < T/\mathrm{K} < 10^{0.3} \Delta T_{\mathrm{AGN}}`).


Power spectra
-------------

.. _issues_power_spectrum:

Normalisation of the matter power spectrum on large scale
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As noted by `Schaller et al. (2025) <https://ui.adsabs.harvard.edu/abs/2025MNRAS.539.1337S/abstract>`__, the total matter
power spectra of the Jet and Jet_fgas-4σ simulations do not exactly match the power spectra of their DMO counterparts on
the largest scales, with an error smaller than 1%.
