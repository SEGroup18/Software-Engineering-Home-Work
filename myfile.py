def compute_perimeter(radius):
    #perimeter formulae = 2 * π * radius
    perimeter = 2 * 3.14 * radius
    return round(perimeter, 2)

def print_info_of_circle(radius):
    perimeter = compute_perimeter(radius)
    print("Radius is : ", radius)
    print("Perimeter is:", perimeter)

def main():
    radius = 5
    print_info_of_circle(radius)
    # undefined variable 'diameter' to showcase error
    print("Diameter is:", 2 * radius)

if __name__ == "__main__":
    main()
    #test
