# Task: convert rows of a table into columns
# Table:
#   Country     City
#   USA         New York
#   USA         Houston
#   USA         Dallas
#   India       Hybera
#   India       Banga
#   India       New Delhi
#   UK          London
#   UK          Bermington
#   UK          Manchester
# Result:
#   Country     City1       City2       City3
#   India       Hybera      Banga       New Delhi
#   UK          London      Bermington  Manchester
#   USA         Mew York    Houston     Dallas
# Code:
    # SELECT * FROM countries
    #
    # SELECT Country, City1, City2, City3
    # FROM (
    #   SELECT Country, City
    #       'City' + CAST(ROW_NUMBER() OVER (PARTITION BY Country ORDER BY Country) AS Varchar(10)) AS ColumnSequence
    #   FROM Countries
    #  ) Temp # name of table = 'Temp'
    #
    # PIVOT (
    #   MAX(City)
    #   FOR ColumnSequence IN (City1, City2, City3)
    # ) Piv

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Write a query to pull all of the members who have a primary home address and show the results. 
# Fields must include: FULL NAME, Address_Line_1, City, State, Zip_Code. 
# A value of 1 in the Primary_Address field indicates that the address is the primary one.
# Tables: 
    # Tbl_Members
    # id_members       First_Name      Last_Name
    # 151                     John            Smith
    # 152                     Karen           Williams
    # 153                     Lee             Johnson

    # Tbl_Address
    # id_address    address_type      primary_address     address_line_1      city    state   zip_code    Tbl_Members_id
    # 1             Home              1                   3321 Green St       Denver  CO      80124       151
    # 2             Work              0                   556 White Drive     Boulder CO      80224       152
    # 3             Home              1                   1246 Greenvile St   Denver  CO      81234       153
# Query:
    # SELECT
    #     CONCAT(First_Name, ' ', Last_Name) AS FULL_NAME,
    #     Address_Line_1 AS Address,
    #     City,
    #     State,
    #     Zip_Code AS Zip
    # FROM
    #     tbl_Members INNER JOIN tbl_address ON 
    #       tbl_Members.id_members = tbl_address.id_address
    # WHERE
    #     primary_address = 1 AND address_type = 'Home'              
# Result:
    # FULL_NAME     Address             City    State   Zip
    # John Smith    3321 Green St       Denver  CO      80124
    # Lee Johnson   1246 Greenvile St   Denver  CO      81234

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Write a running total
# Table Tbl_Stats:
    # UID   GameID  PlayerID    StatType    Stat
    # 1     1       1           Run         3
    # 2     1       1           Run         7
    # 3     1       1           Run         -3    
    # 4     1       1           Run         19
    # 5     1       1           Run         5
    # 6     2       1           Run         15
    # 7     2       1           Run         1
# Query:
    # SELECT
    #     GameID,
    #     PlayerID,
    #     StatType,
    #     Stat,
    #     (SELECT SUM(Stat)
    #      FROM tbl_stats
    #      WHERE 
    #       Stat1.GameID = tbl_stats.GameID AND
    #       stat1.PlayerID = tbl_stats.PlayerID AND 
    #       stat1.stattype = tbl_stats.StatType AND 
    #       tbl_stats.UID <= stat1.UID) AS 'Running Total'
    # FROM
    #     tbl_stats Stat1;
# Result:
    # GameID  PlayerID    StatType    Stat  Running Total
    # 1       1           Run         3     3
    # 1       1           Run         7     10
    # 1       1           Run         -3    7
    # 1       1           Run         19    26
    # 1       1           Run         5     31
    # 2       1           Run         15     15
    # 2       1           Run         1     16

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Write a query to identify Rusty’s grandfather. 
# You can make the assumption that female information in the Parent column is entered prior to the male information. 
# This means the Male information has a greater UID than the female.
# Table Families:
    # UID       Parent      Child
    # 1         'Letha'     'Joyce'
    # 2         'Letha'     'Dick'
    # 3         'Letha'     'Linda'
    # 4         'Letha'     'Donna'
    # 5         'Duck'      'Joyce'
    # 6         'Duck'      'Dick'
    # 7         'Duck'      'Linda'
    # 8         'Duck'      'Donna'
    # 9         'Donna'     'Holly'
    # 10        'Donna'     'Rusty'
    # 11        'Gene'      'Holly'
    # 12        'Gene'      'Rusty'
# Query:
    # SELECT
    #     GrandParent.Parent as GrandFather, Child.Child
    # FROM
    #     Families AS Child 
    #       INNER JOIN 
    #     Families AS GrandParent 
    #       ON Child.Parent = GrandParent.Child
    # WHERE
    #     Child.Child = 'Rusty'
    #     AND GrandParent.uid IN 
    # 		(SELECT
    #             MAX(GrandParent.UID)
    #        FROM
    #             Families AS Child
    #                 INNER JOIN
    #             Families AS GrandParent ON Child.Parent = GrandParent.Child
    #        WHERE
    #             Child.Child = 'Rusty')
# Result:
    # GrandFather   Child
    # Duck          Rusty