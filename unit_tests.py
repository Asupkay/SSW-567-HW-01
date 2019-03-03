from classify_triangle import classify_triangle

class TestTriangles(object):
    """This is a testing class for the classify_triangles method"""

    @staticmethod
    def test_right():
        """Test that right triangles are identified"""
        assert classify_triangle(3, 4, 5) == 'Right'
        assert classify_triangle(6, 8, 10) == 'Right'
        assert classify_triangle(24, 26, 10) == 'Right'

    @staticmethod
    def test_equilateral():
        """Test that equilateral triangles are identified"""
        assert classify_triangle(1, 1, 1) == 'Equilateral'
        assert classify_triangle(100, 100, 100) == 'Equilateral'
        assert classify_triangle(0, 0, 0) != 'Equilateral'

    @staticmethod
    def test_isoceles():
        """Test that isoceles triangles are identified"""
        assert classify_triangle(10, 10, 10) != 'Isoceles'
        assert classify_triangle(5, 5, 3) == 'Isoceles'

    @staticmethod
    def test_scalene():
        """Test that scalene triangles are identified"""
        assert classify_triangle(13, 9, 14) == 'Scalene'
        assert classify_triangle(7.7, 5, 9) == 'Scalene'

    @staticmethod
    def test_not_a_triangle():
        """Test that non triangles are identified"""
        assert classify_triangle(False, 1, 1) == 'NotATriangle'
        assert classify_triangle(100, 1, 1) == 'NotATriangle'
        assert classify_triangle(-1, -1, -1) == 'NotATriangle'
        assert classify_triangle(0, 0, 0) == 'NotATriangle'
