"""
This file contains tests for the molecule module.
"""
import molecool
import numpy as np

def test_compute_molecular_mass():

    symbols = ['C', 'H', 'H', 'H', 'H']

    calculated_mass = molecool.compute_molecular_mass(symbols)

    expected_mass = 16.0107

    # assert expected_mass == calculated_mass

    assert np.isclose(expected_mass, calculated_mass, rtol=1e-2)
