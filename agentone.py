from julep import Julep
import time

def city_facts_workflow():
    """Complete working city facts workflow using Julep"""
    
    print(" City Facts Workflow")
    print("=" * 50)
    
    # Initialize the Julep client
    julep = Julep(api_key="eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkODU5NGE0ZS1kNmM2LTUwMDQtODE0MS05MjQ0MTQyZWY3MjIiLCJlbWFpbCI6ImFudWJoYXZ2ZXJtYWRlbGhpQGdtYWlsLmNvbSIsImlhdCI6MTc0OTM5Njc1NiwiZXhwIjoxNzUwMDAxNTU2fQ.gsV6QU7GQRCleU_NfGu-NisFnq-k4u9QIxaFlpaLgCxo9YSCJ6hBWnPhRy5m6a9lX-AhljPqWBnzslz0jQlNvQ")
    
    try:
        # Create a specialized city facts agent
        agent = julep.agents.create(
            name="City Facts Explorer",
            about="An expert researcher who discovers fascinating, lesser-known facts about cities worldwide from Wikipedia and other reliable sources",
            instructions=[
                "Search for surprising and interesting facts about cities that most tourists don't know",
                "Focus on historical events, unique architecture, cultural oddities, local legends, and unusual statistics",
                "Present facts in an engaging 'Did you know?' format with specific details",
                "Include dates, numbers, and locations when possible to make facts more credible",
                "Avoid common tourist information - dig deeper for hidden gems",
                "Keep facts concise but fascinating"
            ],
            model="gpt-4o-mini",
        )
        
        print(f"✅ Agent created: {agent.name}")
        
        # Create a session for our city research
        session = julep.sessions.create(
            agent=agent.id,
            situation="The user wants to discover amazing, lesser-known facts about cities around the world that would surprise both tourists and locals. Focus on historical events, architectural marvels, cultural oddities, and fascinating statistics.",
        )
        
        print(f"✅ Session created")
        
        # Cities to research (mix of popular and lesser-known)
        cities = [
            "Tokyo", "Paris", "Istanbul", "Cairo", "Prague", 
            "Kyoto", "Barcelona", "Amsterdam", "Vienna", "Marrakech"
        ]
        
        print(f"\n🚀 Researching {len(cities)} fascinating cities...\n")
        
        all_facts = {}
        
        for i, city in enumerate(cities, 1):
            print(f"📍 Researching {city} ({i}/{len(cities)})...")
            
            try:
                # Create a detailed prompt for each city
                prompt = f"""Please research {city} and give me 3 absolutely fascinating "Did you know?" facts about this city that would surprise most people.

Focus on:
- Historical events or famous figures with interesting stories
- Unique architecture or landmarks with surprising backstories  
- Local legends, cultural oddities, or unusual traditions
- Geographical features or city planning quirks
- Interesting statistics, records, or unusual facts

Format your response like this:

🏙️ **{city} - Hidden Gems & Fascinating Facts**

🤔 **Did you know?** [Amazing fact #1 with specific details like dates, numbers, or locations]

🤔 **Did you know?** [Incredible fact #2 with surprising backstory or context]

🤔 **Did you know?** [Mind-blowing fact #3 with interesting details]

Make each fact genuinely surprising - avoid common tourist knowledge!"""

                # Get response from the agent
                response = julep.sessions.chat(
                    session_id=session.id,
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )
                
                # Extract the content from the response
                if response.choices and len(response.choices) > 0:
                    content = response.choices[0].message.content
                    all_facts[city] = content
                    
                    print("✅ Facts discovered!")
                    print("-" * 60)
                    print(content)
                    print("-" * 60)
                    print()
                else:
                    print(f"❌ No response received for {city}")
                
                # Small delay to be respectful to the API
                time.sleep(2)
                
            except Exception as e:
                error_msg = f"❌ Error researching {city}: {str(e)}"
                print(error_msg)
                all_facts[city] = error_msg
                print()
        
        # Summary
        print("🎉 Research Complete!")
        print("=" * 50)
        print(f"Successfully researched {len([f for f in all_facts.values() if not f.startswith('❌')])} cities")
        print(f"Total facts discovered: {len([f for f in all_facts.values() if not f.startswith('❌')]) * 3}")
        
        # Optional: Save results to file
        save_to_file = input("\n💾 Save results to file? (y/n): ").lower().strip()
        if save_to_file == 'y':
            filename = "city_facts_results.txt"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("🌍 Amazing City Facts - Discovered by Julep AI\n")
                f.write("=" * 60 + "\n\n")
                
                for city, facts in all_facts.items():
                    f.write(f"{facts}\n\n")
            
            print(f"✅ Results saved to {filename}")
    
    except Exception as e:
        print(f"❌ Workflow failed: {str(e)}")
        import traceback
        traceback.print_exc()

def quick_test():
    """Quick test with just one city"""
    print("🚀 Quick Test - Single City")
    
    julep = Julep(api_key="eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkODU5NGE0ZS1kNmM2LTUwMDQtODE0MS05MjQ0MTQyZWY3MjIiLCJlbWFpbCI6ImFudWJoYXZ2ZXJtYWRlbGhpQGdtYWlsLmNvbSIsImlhdCI6MTc0OTM5Njc1NiwiZXhwIjoxNzUwMDAxNTU2fQ.gsV6QU7GQRCleU_NfGu-NisFnq-k4u9QIxaFlpaLgCxo9YSCJ6hBWnPhRy5m6a9lX-AhljPqWBnzslz0jQlNvQ")
    
    try:
        agent = julep.agents.create(
            name="City Explorer",
            about="Finds amazing facts about cities",
            model="gpt-4o-mini"
        )
        
        session = julep.sessions.create(
            agent=agent.id,
            situation="User wants surprising city facts"
        )
        
        city = "Venice"
        response = julep.sessions.chat(
            session_id=session.id,
            messages=[{
                "role": "user", 
                "content": f"Give me 3 amazing facts about {city} that would surprise tourists!"
            }]
        )
        
        print(f"\n🏙️ {city} Facts:")
        print("-" * 30)
        print(response.choices[0].message.content)
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("Choose option:")
    print("1. Full workflow (10 cities)")
    print("2. Quick test (1 city)")
    
    choice = input("Enter 1 or 2: ").strip()
    
    if choice == "1":
        city_facts_workflow()
    else:
        quick_test()