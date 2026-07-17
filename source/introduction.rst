Introduction
============

This service provides web based remote access to the `FLAMINGO
simulations <https://flamingo.strw.leidenuniv.nl/>`__ described in
`Schaye et al (2023)
<https://ui.adsabs.harvard.edu/abs/2023MNRAS.526.4978S/abstract>`__
and `Kugel et al (2023)
<https://ui.adsabs.harvard.edu/abs/2023MNRAS.526.6103K/abstract>`__.
The FLAMINGO data release is presented in `Helly et al (2026)
<https://ui.adsabs.harvard.edu/abs/2026A%26C....5701159H/abstract>`__.

FLAMINGO simulation data products
---------------------------------

The following data products are available:

  * :doc:`snapshots/index` of the full distribution of particles (dark
    matter, gas, stars, black holes and neutrinos) at a :doc:`series
    of output times <snapshots/snapshot_redshifts>` between redshift
    z=15 and the present day
  * Halo catalogues and merger trees generated using the `HBT-HERONS
    <https://hbt-herons.strw.leidenuniv.nl/>`__ halo finder (`Forouhar
    Moreno et al. 2025
    <https://ui.adsabs.harvard.edu/abs/2025arXiv250206932F/abstract>`__)
    with a wide range of halo properties computed using the `SOAP
    <https://joss.theoj.org/papers/10.21105/joss.08252>`__
    post-processing tool (`McGibbon et al. 2025
    <https://ui.adsabs.harvard.edu/abs/2025JOSS...10.8252M/abstract>`__.)
  * Full sky :doc:`lightcone particle
    outputs<lightcones/particle_lightcones>`, where each simulation
    particle is output as it crosses the past lightcone of an observer
    placed somewhere in the simulation volume
  * Full sky :doc:`HEALPix maps <lightcones/healpix_lightcones>` of
    various quantities evaluated in spherical shells around each
    lightcone observer. These include the total mass in gas, stars and
    dark matter, the X-ray luminosity of the gas in several bands,
    measurements of the thermal and kinetic Sunyaev–Zeldovich effects,
    the dispersion measure and weak lensing convergence.
  * Approximate :doc:`lightcone halo
    catalogues<lightcones/halo_lightcones>` created by using black
    hole particles to trace halo positions between snapshots

Documentation
-------------

See the links in the side bar on the left for :doc:`more information
on how to use this service <service_docs/index>` and full descriptions
of the available data products.

Downloading simulation data
---------------------------

All outputs are stored in the form of HDF5 files. Complete files and
directories (such as a full simulation snapshot or a halo catalogue)
can be downloaded directly for local analysis. We provide a `web-based
file browser <viewer.html?path=FLAMINGO>`__ which can be used to
locate files of interest and view their contents.

.. image:: images/L1_m9_directory.png
   :class: screenshot
   :alt: screenshot of the file browser page

Accessing subsets of the data
-----------------------------

We also provide a mechanism to request parts of HDF5 files without
downloading the whole file. This allows more granular access: it is
possible, for example, to download just the star particles from some
specified region in a simulation snapshot or download only a few
properties of interest from a halo catalogue.

We provide an adapted version of the `swiftsimio
<https://swiftsimio.readthedocs.io/en/latest/loading_data/index.html>`__
python module which can transparently make use of this service, and a
more generic :doc:`hdfstream <service_docs/python_module>` module
which allows downloads of arbitrary HDF5 data using a similar
interface to h5py. We also plan to adapt `pynbody
<https://github.com/pynbody/pynbody>`__ to access this service.

.. image:: images/download_dataset.gif
   :class: screenshot
   :alt: animation showing a dataset download in python
