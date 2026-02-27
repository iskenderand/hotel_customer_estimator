import pandas as pd

# Display settings (show all columns and more rows)
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)

# Reading the Excel file
df = pd.read_excel("C:/Users/isken/OneDrive/Masaüstü/miuul_gezinomi.xlsx")


# ---------------- DATAFRAME GENERAL CHECK FUNCTION ----------------
def check_df(dataframe, head=5, tail=5):

    # Dataset shape (rows, columns)
    print("##################### Shape #####################")
    print(dataframe.shape)

    # Variable data types
    print("##################### Types #####################")
    print(dataframe.dtypes)

    # First observations
    print("##################### Head #####################")
    print(dataframe.head(head))

    # Last observations
    print("##################### Tail #####################")
    print(dataframe.tail(tail))

    # Missing value check
    print("##################### NA #####################")
    print(dataframe.isnull().sum())


# Inspect dataset
check_df(df)


# ---------------- EARLY BOOKING SCORE CREATION ----------------
# Create segments based on how many days before check-in the purchase was made
df["EB_Score"] = pd.cut(
        df["SaleCheckInDayDiff"],
        bins=[0, 7, 30, 90, df["SaleCheckInDayDiff"].max()],
        labels=["Last Minuters", "Potential Planners", "Planners", "Early Bookers"]
)

# Frequency of created segments
df["EB_Score"].value_counts()


# ---------------- AVERAGE PRICE AGGREGATION ----------------
# Calculate average price by City + Concept + Season breakdown
agg_df = pd.DataFrame(
    df.groupby(["SaleCityName", "ConceptName", "Seasons"])
      .agg({"Price": "mean"})
).sort_values(by=["Price"], ascending=False)

# Reset index to convert indices back into columns
agg_df = agg_df.reset_index()


# ---------------- SALES LEVEL BASED PERSONA CREATION ----------------
# Create customer/persona key by combining categorical variables
agg_df["sales_level_based"] = agg_df[
    ["SaleCityName", "ConceptName", "Seasons"]
].agg(lambda x: "_".join(x).upper(), axis=1)


# ---------------- SEGMENT CREATION ----------------
# Create 4 equal segments (quartiles) based on average prices
agg_df["SEGMENT"] = pd.qcut(
    agg_df["Price"],
    4,
    labels=["D", "C", "B", "A"]   # A = highest price segment
)


# Price statistics by segment
df.groupby(agg_df["SEGMENT"]).agg({"Price": ["mean", "max", "min"]})


# ---------------- NEW USER ESTIMATION ----------------
# Persona information of a new incoming user
new_user = "ANTALYA_HERŞEY DAHIL_HIGH"

# Find which segment and average price this user belongs to
agg_df[agg_df["sales_level_based"] == new_user]