#!/usr/bin/env python3
# filepath: /home/jbn/holbertonschool-web_front_end/python-server_side_rendering/task_00_intro.py
import os

def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template and a list of attendees.
    
    Args:
        template (str): The template string with placeholders.
        attendees (list): A list of dictionaries containing attendee information.
        
    Returns:
        None
    """
    # Check if template is a string
    if not isinstance(template, str):
        print(f"Error: Template must be a string, got {type(template).__name__}")
        return
    
    # Check if attendees is a list
    if not isinstance(attendees, list):
        print(f"Error: Attendees must be a list, got {type(attendees).__name__}")
        return
    
    # Check if each item in attendees is a dictionary
    for attendee in attendees:
        if not isinstance(attendee, dict):
            print(f"Error: Each attendee must be a dictionary, got {type(attendee).__name__}")
            return
    
    # Check if template is empty
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    
    # Check if attendees list is empty
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    # Process each attendee
    for i, attendee in enumerate(attendees, 1):
        try:
            # Create a copy of the template for this attendee
            output_text = template
            
            # Replace placeholders with values
            for key in ["name", "event_title", "event_date", "event_location"]:
                # Get value, use "N/A" if missing or None
                value = attendee.get(key)
                if value is None:
                    value = "N/A"
                
                # Replace placeholder in template
                placeholder = "{" + key + "}"
                output_text = output_text.replace(placeholder, str(value))
            
            # Write to output file
            output_file = f"output_{i}.txt"
            
            # Check if file already exists
            if os.path.exists(output_file):
                print(f"Warning: File {output_file} already exists. Overwriting.")
            
            with open(output_file, "w") as f:
                f.write(output_text)
                
        except Exception as e:
            print(f"Error processing attendee {i}: {str(e)}")

if __name__ == "__main__":
    # Example template
    template = """Hello {name},

You are invited to the {event_title} on {event_date} at {event_location}.

We look forward to your presence.

Best regards,
Event Team"""

    # Example attendees
    attendees = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]
    
    # Call the function
    generate_invitations(template, attendees)