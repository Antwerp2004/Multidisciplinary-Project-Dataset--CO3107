import pandas as pd

# Load the CSV file
csv_file = "Data/Garden.csv"  # Replace with your CSV file
output_sql_file = "Data/Garden.sql"  # Output SQL file
table_name = "Garden"  # Your MySQL table name

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file, encoding='utf-8-sig')

# Generate SQL statements
with open(output_sql_file, "w", encoding="utf-8") as f:
    # Write the header with the table name
    f.write(f"INSERT INTO \"{table_name}\" ({', '.join(f'\"{col}\"' for col in df.columns)}) VALUES\n")

    # Iterate through rows and write values
    for i, row in df.iterrows():
        # Prepare the row values, adding quotes for strings and handling NULLs
        values = []  # Reset values for each row
        for value in row:
            if pd.isna(value):  # Handle NULL values
                values.append("NULL")
            elif isinstance(value, (int, float)):  # Numeric values
                values.append(str(value))
            else:  # String values
                # Escape single quotes for SQL syntax and wrap the value in quotes
                escaped_value = str(value).replace("'", "\\'")
                values.append(f"'{escaped_value}'")

        # Write the row into the SQL file
        row_sql = f"({', '.join(values)})"
        if i < len(df) - 1:
            row_sql += ","  # Add a comma except for the last row
        else:
            row_sql += ";"  # Finalize the last row with a semicolon
        row_sql += "\n"  # Add a newline character
        f.write(row_sql)

print(f"SQL file has been generated: {output_sql_file}")