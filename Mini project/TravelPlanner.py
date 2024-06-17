class ItineraryPlanner:
    def __init__(self):
        self.itinerary = {}

    def add_destination(self, destination):
        if destination in self.itinerary:
            print(f"{destination} is already in your itinerary.")
        else:
            self.itinerary[destination] = []
            print(f"Added {destination} to your itinerary.")

    def add_activity(self, destination, activity):
        if destination in self.itinerary:
            self.itinerary[destination].append(activity)
            print(f"Added activity '{activity}' to {destination}.")
        else:
            print(f"{destination} is not in your itinerary. Please add it first.")

    def view_itinerary(self):
        if not self.itinerary:
            print("Your itinerary is empty.")
        else:
            for destination, activities in self.itinerary.items():
                print(f"\nDestination: {destination}")
                if activities:
                    for idx, activity in enumerate(activities, 1):
                        print(f"  {idx}. {activity}")
                else:
                    print("  No activities planned.")

def main():
    planner = ItineraryPlanner()
    
    while True:
        print("\nTravel Itinerary Planner")
        print("1. Add Destination")
        print("2. Add Activity")
        print("3. View Itinerary")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            destination = input("Enter the destination: ")
            planner.add_destination(destination)
        elif choice == '2':
            destination = input("Enter the destination: ")
            activity = input("Enter the activity: ")
            planner.add_activity(destination, activity)
        elif choice == '3':
            planner.view_itinerary()
        elif choice == '4':
            print("Exiting the Travel Itinerary Planner. Safe travels!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
