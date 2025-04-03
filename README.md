# EERD link
https://drive.google.com/file/d/1EkanKVxXPVithBIEh8e4cu040yx-KggT/view?usp=sharing

# Some explanation of the tables' current data
- `User`: 5 users, password encrypted.
- `Garden`: 2 gardens, name is concatenated.
- `has`: Each garden has 1-5 users (Geometric distribution 0.5).
- `Report`: Report every 30 seconds, start from 1/1/2025.
- `ChangeLog`:
1. Base on the conditions of each entry in `Report` table, then apply threshold to determine the action at that time.
2. Approx 3% of the Report has values under THRESHOLD.
3. The implementation time is in TIME_OFFSET (curently +5 seconds each).
- `Warnings`: Adjust: Tuple (Username, Time_created, Description) is the Primary Key.
1. Approx 10% of the ChangeLog has malfunctions.
2. Randomly select between 2 warnings in the respective category.
3. Send warning to all the users of that garden.