from myfile import compute_perimeter

def test_compute_perimeter():
    assert compute_perimeter(5) == 31.4

def test_compute_perimeter_fails():
    assert compute_perimeter(5) == 31.42