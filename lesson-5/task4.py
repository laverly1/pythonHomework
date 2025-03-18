import statistics

def enrollment_stats(universities):
    """Returns two lists: student enrollments and tuition fees."""
    enrollments = [uni[1] for uni in universities]
    tuitions = [uni[2] for uni in universities]
    return enrollments, tuitions

def mean(values):
    """Returns the mean of a list of values."""
    return sum(values) / len(values)

def median(values):
    """Returns the median of a list of values."""
    return statistics.median(values)

def main():
    universities = [
        ['California Institute of Technology', 2175, 37704],
        ['Harvard', 19627, 39849],
        ['Massachusetts Institute of Technology', 10566, 40732],
        ['Princeton', 7802, 37000],
        ['Rice', 5879, 35551],
        ['Stanford', 19535, 40569],
        ['Yale', 11701, 40500]
    ]
    
    enrollments, tuitions = enrollment_stats(universities)
    
    total_students = sum(enrollments)
    total_tuition = sum(tuitions)
    student_mean = mean(enrollments)
    student_median = median(enrollments)
    tuition_mean = mean(tuitions)
    tuition_median = median(tuitions)
    
    print("*" * 30)
    print(f"Total students: {total_students:,}")
    print(f"Total tuition: $ {total_tuition:,}")
    print("\nStudent mean: {:.2f}".format(student_mean))
    print(f"Student median: {int(student_median):,}")
    print("\nTuition mean: $ {:.2f}".format(tuition_mean))
    print(f"Tuition median: $ {int(tuition_median):,}")
    print("*" * 30)

if __name__ == "__main__":
    main()