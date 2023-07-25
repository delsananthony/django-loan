from django.db import ProgrammingError, connection, models
from datetime import date


class Member(models.Model):
    firstname = models.CharField(verbose_name="Firstname", max_length=255)
    lastname = models.CharField(verbose_name="Lastname", max_length=255)
    middlename = models.CharField(verbose_name="Middlename", max_length=255)
    date_created = models.DateField(verbose_name="Date Created", default=date.today)

    def get_customer_records(self):
        try:
            with connection.cursor() as cursor:
                # Write your raw SQL query here
                sql_query = "SELECT * FROM Member;"
                cursor.execute(sql_query)

                # Fetch the results (if needed)
                results = cursor.fetchall()

                return results
                # for row in results:
                #     # Process the data here
                #     print(row)
        except ProgrammingError as e:
            # Handle any exceptions or errors
            print(f"Error executing SQL query: {e}")
