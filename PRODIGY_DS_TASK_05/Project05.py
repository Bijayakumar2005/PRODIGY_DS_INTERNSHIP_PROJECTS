import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap

def analyze_uk_accidents(filepath):
    try:
        # Load the dataset
        df = pd.read_csv(filepath, low_memory=False)
        print(f"Dataset loaded with {len(df):,} records")
        
        # Display available columns
        print("\nAvailable columns:")
        print(df.columns.tolist())
        
        # Convert date/time (adjust column names as needed)
        time_col = 'Date' if 'Date' in df.columns else 'Accident_Date'
        df['DateTime'] = pd.to_datetime(df[time_col])
        
        # Extract time features
        df['Hour'] = df['DateTime'].dt.hour
        df['DayOfWeek'] = df['DateTime'].dt.dayofweek
        df['Month'] = df['DateTime'].dt.month
        day_names = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        
        # Set up visualization style
        plt.style.use('ggplot')
        sns.set_palette("pastel")
        
        # 1. Temporal Analysis
        plt.figure(figsize=(18, 14))
        
        # Hourly pattern
        plt.subplot(3, 2, 1)
        sns.countplot(x='Hour', data=df)
        plt.title('Accidents by Hour of Day')
        
        # Weekly pattern
        plt.subplot(3, 2, 2)
        sns.countplot(x='DayOfWeek', data=df)
        plt.xticks(ticks=range(7), labels=day_names, rotation=45)
        plt.title('Accidents by Day of Week')
        
        # Monthly pattern
        plt.subplot(3, 2, 3)
        month_order = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        sns.countplot(x='Month', data=df)
        plt.xticks(ticks=range(12), labels=month_order)
        plt.title('Accidents by Month')
        
        # 2. Weather Impact Analysis
        if 'Weather_Conditions' in df.columns:
            plt.subplot(3, 2, 4)
            weather_counts = df['Weather_Conditions'].value_counts().head(10)
            weather_counts.plot(kind='bar')
            plt.title('Top 10 Weather Conditions')
            plt.xticks(rotation=45)
        
        # 3. Road Conditions Analysis
        if 'Road_Surface_Conditions' in df.columns:
            plt.subplot(3, 2, 5)
            road_conditions = df['Road_Surface_Conditions'].value_counts()
            road_conditions.plot(kind='bar')
            plt.title('Road Surface Conditions')
            plt.xticks(rotation=45)
        
        # 4. Accident Severity
        if 'Accident_Severity' in df.columns:
            plt.subplot(3, 2, 6)
            severity_counts = df['Accident_Severity'].value_counts()
            severity_counts.plot(kind='pie', autopct='%1.1f%%')
            plt.title('Accident Severity Distribution')
            plt.ylabel('')
        
        plt.tight_layout()
        plt.show()
        
        # Hotspot Analysis - will open in browser
        if all(col in df.columns for col in ['Latitude', 'Longitude']):
            print("\nPreparing accident hotspot map... (will open in browser)")
            
            # Create base map
            uk_center = [54.5, -2.5]  # Approximate UK center
            hotspot_map = folium.Map(location=uk_center, zoom_start=6)
            
            # Filter valid coordinates
            valid_coords = df.dropna(subset=['Latitude', 'Longitude'])
            locations = valid_coords[['Latitude', 'Longitude']].values.tolist()
            
            # Add heatmap
            HeatMap(locations, radius=10, blur=15).add_to(hotspot_map)
            
            # For non-notebook environments, this will open in browser
            return hotspot_map  # Return the map object
        
        return None

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return None

# Example usage:
if __name__ == "__main__":
    # Run analysis
    result_map = analyze_uk_accidents('PRODIGY_DS_INTERNSHIP_PROJECTS/PRODIGY_DS_TASK_05/Accident_Information.csv')
    
    # If you want to automatically open the map in browser
    if result_map:
        print("\nTo view the interactive map, check your browser or use:")
        print("result_map.show_in_browser()")