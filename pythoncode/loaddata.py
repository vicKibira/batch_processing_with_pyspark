import os
import time

class DownloadData():
    def __init__(self, years, months, colors):
        self.years = years
        self.months = months
        self.colors = colors

    def pull_data_from_web(self):  # Add self here
        print("Downloading data...\n")

        for year in self.years:  # Access years via self
            for month in self.months:  # Access months via self
                for color in self.colors:  # Access colors via self

                    time_start = time.time()
                    try:

                        url = f"https://github.com/DataTalksClub/nyc-tlc-data/releases/download/{color}/{color}_tripdata_{year}-{month:02}.csv.gz"

                        filename = f"{color}/{color}_tripdata_{year}-{month:02}.csv.gz"

                        os.makedirs(os.path.dirname(filename), exist_ok=True) #make a directory if it does not exist
                        os.system(f"wget {url} -O {filename}")  # Silence wget output

                        print(f"Downloaded {color} data for {year}-{month:02}.")

                    except Exception as e:
                        print(f"Oops an error occurred while downloading {color} data for {year}-{month:02}: {e}")

                    time_end = time.time()
                    print(f"Time taken: {time_end - time_start:.2f} seconds.\n")
                    
        print("All data downloaded successfully.")

if __name__ == "__main__":
    
    years = [2019, 2020]
    months = range(1, 2)  # Only January
    colors = ['yellow', 'green']

    data = DownloadData(years, months, colors)
    data.pull_data_from_web()
