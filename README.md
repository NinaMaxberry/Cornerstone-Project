# KY GERRYMANDERING PROJECT PLAN

# Purpose

Allow user input to compare the transition/change (if any) in congressional voting districts utilizing census data for the years 2000 and 2010, effective for 2019 reporting year.
++Guesstimate of 2020 redistricting based on median/averages of 2000 and 2010 data
++Compare change in household size/education/household income per census year

##   Technical Summary

Django – framework – front end
Python - programming
SQL – managing DB’s/reporting
Map Plotting (i.e. Matplotlib. etc.)-state of KY map and overlays of districts(?)
Bootstrap- front end


##   Features

## Start page
    # Welcome <header>
            i.	Constants
                1.	Background information regarding all districts
                    a.  How many districts
                    b.	List for 2000 and 2010
                    c.	Print for each year
            2.	Total senators and representatives in KY
                    a.	List for 2000 and 2010
                    b.	Print for each year
            3.	Disclaimer - Print: “Due to term limits, terms for some may have ended or begun between the years available in this study.” </header>

            ii.	User zip code input
                1.	Zip Code Validation
                    a.	Ensure zip exists in KY
                2.	Requirements
                    a.	DB of all zip codes in Kentucky
                    b.	Create DB to match zip codes with districts
                    c.	Need DB listing counties in district selected
                        i.	Fields
                            1.	District ID(?)
                            2.	District # (primary key)
                            3.	Zip Code
                            4.	Counties
                            5.	Year (2000 and 2010)
                            6.	++email address – to thank for visiting


## New Page from user input
                a.	Two maps of Kentucky (one for each census year)
                    i.	Overlay of district chosen (outlined)
                            1.	Requirements
                                a.	Query zip DB grouping districts per year
                                    i.	Fields
                                        1.	Rep Table Per Year
                                            a.	ID# for each rep
                                            b.	Name
                                            c.	District
                                            d.	Zip Code
                            2.	Senate Table Per Year
                                a.	ID# for each rep
                                b.	Name
                                c.	District
                                d.	Zip Code
                b.	Need interactive map
                    i.	Code needed to populate maps separately
                        1.	Requirements
                            a.	???????
                    ii.	List of senators and reps in that selected district
                        1.	Requirements
                            a.	DB for each district with reps and senators
                                i.	Fields
                                    1.	Name
                                    2.	District
                            b.	Produce names of reps and senators
                            c.	++images, how long served and when term ends
                            d.	++separate pop-out of selected rep with profile
                b.	Table (additional information)
                    i.	Demographic Changes (education and household income)
                        1.	Comparison of two data points for each year
                            a.	Requirements
    3.	Resources – provide links (new page)
    4.	++Provide user comments area (blog-like)
        a.	If added will need input area for user to register and enter comment



