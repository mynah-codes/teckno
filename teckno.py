import pandas as pd
import matplotlib.pyplot as plt
from ast import literal_eval

## DATA PREPARATION
print("** DATA PREPARATION **\n")

# Sample data for purchasing habits and online presence of Gen Z in Ireland
purchasing_data = {
    "row_1": ["John", "15", "Male", "Cork", ("Video Games", "Runners"), ("Youtube", "TikTok")],
    "row_2": ["Alison", "35", "Female", "Dublin", ("Skincare", "Loungewear"), ("Instagram", "Email")],
    "row_3": ["Riley", "17", "Prefer not to say", "Galway", ("Shoes", "Clothes"), ("Snapchat", "TikTok")],
    "row_4": ["Tara", "21", "Female", "Cork", ("Books", "Video Games"), ("TikTok", "X")],
    "row_5": ["Eoghan", "39", "Male", "Galway", ("Race tickets", "Gifts"), ("Facebook", "Email")],
    "row_6": ["Anna", "15", "Female", "Dublin", ("Loungewear", "Dog Treats"), ("Snapchat", "Youtube")],
    "row_7": ["Jordan", "16", "Prefer not to say", "Cork", ("Skincare", "Runners"), ("TikTok", "Youtube")],
    "row_8": ["Emily", "14", "Female", "Galway", ("Dog Treats", "Shoes"), ("Snapchat", "TikTok")],
    "row_9": ["Caoimhe", "29", "Female", "Cork", ("Gig tickets", "Clothes"), ("Instagram", "Youtube")],
    "row_10": ["Ahmed", "17", "Male", "Galway", ("Clothes", "Video Games"), ("X", "Snapchat")]
}

df = pd.DataFrame(purchasing_data).T # Create a DataFrame from the purchasing data
df.columns = ["Name", "Age", "Gender", "Location", "Social Media Purchases", "Online Presence"] # Rename the columns for better readability

# ALTERNATIVE TO DATA UPLOAD: delete the lines above, and uncomment line below
# df = pd.read_csv("https://raw.githubusercontent.com/mynah-codes/teckno/main/purchasing_data.csv")
print(df) # Display the DataFrame

# Count the frequency of each product category in the purchasing habits
product_categories = [] # Initialize an empty list to store product categories
for purchases in df["Social Media Purchases"]: # For loop iterates over the "Social Media Purchases" column in the DataFrame, where each entry is a tuple of product categories.
    if isinstance(purchases, str): # This if case handles converting string literal tuples in csv data import, instead of using dictionary
        purchases = literal_eval(purchases)
    product_categories.extend(purchases) # The extend() method is used to add the elements of the purchases tuple to the product_categories list, effectively flattening the list of categories.

print(f"\nAll Product Categories Purchased: {product_categories}") # Print the list of all product categories purchased by the respondents

# Create a Pandas Series from the product_categories list and use the value_counts() method to count the frequency of each unique product category.
categories = pd.Series(product_categories) # Create a Pandas Series from the product_categories list
print(f"\nUnique Product Categories: {categories.unique()}") # Print the unique product categories

category_counts = categories.value_counts() # The result is stored in the category_counts variable, which is a Series where the index represents the unique product categories and the values represent their respective counts.
print("\nProduct Category Counts:")
print(category_counts)

# Create a bar chart to visualize the product category counts
category_counts.plot.bar()
plt.show()

## EXERCISES: DO SIMILAR ANALYSIS, COUNTING UP NUMBERS FOR AGE GROUPS, COUNTIES, SOCIAL MEDIA PLATFORMS
## AGE GROUP ANALYSIS
print("\n** AGE GROUP ANALYSIS **")

df["Age"] = df["Age"].astype(int) # Convert the "Age" column to integers for easier analysis
# ...rest of the code

## COUNTY ANALYSIS
print("\n** COUNTY ANALYSIS **")
# ...rest of the code

## SOCIAL MEDIA ANALYSIS
print("\n** SOCIAL MEDIA ANALYSIS **")
# ...rest of the code

## DUBLIN SPECIFIC ANALYSIS: COUNTS OF PURCHASES MADE BY PEOPLE IN DUBLIN ONLY
print("\n** DUBLIN SPECIFIC PURCHASE ANALYSIS **")
# ...rest of the code
