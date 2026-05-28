import pandas as pd
import matplotlib.pyplot as plt

## DATA PREPARATION
print("\n** DATA PREPARATION **")

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
print(df) # Display the DataFrame

## PRODUCT CATEGORY ANALYSIS
print("\n** PRODUCT PURCHASE ANALYSIS**")

# Count the frequency of each product category in the purchasing habits
product_purchases = [] # Initialize an empty list to store product purchase types
for purchases in df["Social Media Purchases"]: # For loop iterates over the "Social Media Purchases" column in the DataFrame, where each entry is a tuple of product categories.
    product_purchases.extend(purchases) # The extend() method is used to add the elements of the purchases tuple to the product_categories list, effectively flattening the list of categories.

print(f"\nAll Product Categories Purchased: {product_purchases}") # Print the list of all product categories purchased by the respondents

# Create a Pandas Series from the product_categories list and use the value_counts() method to count the frequency of each unique product category.
purchase_categories = pd.Series(product_purchases) # Create a Pandas Series from the product_categories list
print(f"\nUnique Product Categories: {purchase_categories.unique()}") # Print the unique product categories

purchase_category_counts = purchase_categories.value_counts() # The result is stored in the category_counts variable, which is a Series where the index represents the unique product categories and the values represent their respective counts.
print("\nProduct Category Counts:")
print(purchase_category_counts)

# Create a bar chart to visualize the product category counts
purchase_category_counts.plot.bar()
plt.show()

## AGE GROUP ANALYSIS
print("\n** AGE GROUP ANALYSIS **")

df["Age"] = df["Age"].astype(int) # Convert the "Age" column to integers for easier analysis

# Create age group labels
age_groups = []

for age in df["Age"]:
    if age < 18:
        age_groups.append("Teenager")
    elif age <= 30:
        age_groups.append("18-30")
    else:
        age_groups.append("30-40")

# Count each group
age_counts = pd.Series(age_groups).value_counts()

print(age_counts)

# Create bar chart
age_counts.plot.bar()
plt.show()

## COUNTY ANALYSIS
print("\n** COUNTY ANALYSIS **")

# Count the frequency of each location in the DataFrame
location_counts = df["Location"].value_counts()
print(location_counts) # Print the counts of each location

# Create a bar chart to visualize the location counts
location_counts.plot.bar()
plt.show()

## SOCIAL MEDIA ANALYSIS
print("\n** SOCIAL MEDIA ANALYSIS **")

# Count the frequency of each social media platform in the online presence column
social_media_platforms = [] # Initialize an empty list to store social media platforms
for platforms in df["Online Presence"]: # For loop iterates over the "Online Presence"
    social_media_platforms.extend(platforms)

social_media_counts = pd.Series(social_media_platforms).value_counts()
print(f"\nSocial Media Platform Counts:\n{social_media_counts}") # Print the counts

# Create a bar chart to visualize the social media platform counts
social_media_counts.plot.bar()
plt.show()

## DUBLIN SPECIFIC ANALYSIS: COUNTS OF PURCHASES MADE BY PEOPLE IN DUBLIN ONLY
print("\n** DUBLIN SPECIFIC PURCHASE ANALYSIS **")

# Now count highest purchase counts from people only in Dublin, first by getting all the people only in Dublin
dublin_df = df[df["Location"] == "Dublin"]

# Store all purchases here
dublin_categories = []

# Loop through the purchases column
for purchases in dublin_df["Social Media Purchases"]:
    dublin_categories.extend(purchases)

# Count each purchase category
dublin_category_counts = pd.Series(dublin_categories).value_counts()

print(f"\nPurchase counts in Dublin: {dublin_category_counts}")

# Create a bar chart to visualize the product category counts
dublin_category_counts.plot.bar()
plt.show()
