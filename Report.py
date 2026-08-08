# Dynamic Report Generator using OOP in Python
# Concepts Used:
# 1. Decorators
# 2. Class Methods
# 3. Magic Methods

# Decorator to add a header and footer to the report
def report_decorator(func):
    def wrapper(*args, **kwargs):
        print("\n" + "=" * 40)
        print("        DYNAMIC REPORT")
        print("=" * 40)

        # Call the original report method
        func(*args, **kwargs)

        print("=" * 40)
        print("         END OF REPORT")
        print("=" * 40)
    return wrapper


# Report Class
class Report:

    # Class variable (shared by all objects)
    company_name = "ABC Solutions"

    # Constructor
    def __init__(self, title, content):
        self.title = title
        self.content = content

    # Class Method
    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name

    # Magic Method - String Representation
    def __str__(self):
        return f"Report Title: {self.title}"

    # Magic Method - Length of Report Content
    def __len__(self):
        return len(self.content)

    # Display Report
    @report_decorator
    def display_report(self):
        print(f"Company : {Report.company_name}")
        print(f"Title   : {self.title}")
        print("-" * 40)
        print(self.content)
        print("-" * 40)
        print(f"Content Length : {len(self)} characters")

3
# Main Program 

# Create report objects
report1 = Report(
    "Monthly Sales Report",
    "Total Sales: Rs. 2,50,000\nProfit: Rs. 80,000"
)

report2 = Report(
    "Student Attendance Report",
    "Attendance: 92%\nStudents Present: 46"
)

# Display report using magic method (__str__)
print(report1)

# Display first report
report1.display_report()

# Change company name using class method
Report.change_company("XYZ Technologies")

# Display second report
report2.display_report()