

def build_roster(registrations):
    """
    Given a list of (student_id, course_id) pairs, build a course roster.

    The result should be a dictionary where:
      - each key is a course id (string)
      - each value is a sorted list of unique student ids (strings)
        enrolled in that course

    Duplicate registrations for the same (student_id, course_id) pair
    should appear only once in the output.
    """

    # Group registrations by course using a dictionary with sets to track unique students
    roster = {}
    for student_id, course_id in registrations:
        if course_id not in roster:
            roster[course_id] = set()
        roster[course_id].add(student_id)
    
    # Convert sets to sorted lists
    for course_id in roster:
        roster[course_id] = sorted(roster[course_id])
    
    return roster


if __name__ == "__main__":
    # Optional manual test
    sample = [
        ("s1", "CS101"),
        ("s2", "CS101"),
        ("s1", "MATH200"),
        ("s1", "CS101"),
    ]
    print(build_roster(sample))
