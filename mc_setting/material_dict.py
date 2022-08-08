def materials():
    """material dictionary, values in HU.
    Materials: 'Air','Fat','Water','Nylon','Polyethylene','Teflon','Acrylic','Lexan','Copper'

    Returns:
        dict: how to use, m['Water']
    """
    # https://en.wikipedia.org/wiki/Hounsfield_scale
    # https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8511832/
    # https://www.ctug.org.uk/meet08-10-21/CT%20Numbers%20-%20A%20problem.pdf
    material = ['Air','Fat','Water','Nylon','Polyethylene','Teflon','Acrylic','Lexan','Copper']
    HounsfieldUnit = [-1000, -105, 0, 100, -75, 1017, 140, 116, 14000]
    m = dict(zip(material,HounsfieldUnit))
    return m