#!/usr/bin/env python3
"""
Hyderabad Culture Assistant
A simple AI-powered tool using custom context about Hyderabad
"""

import os
import sys


def load_context(file_path=".kiro/product.md"):
    """Load Hyderabad context from the product.md file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: Context file '{file_path}' not found!")
        sys.exit(1)


def search_context(query, context):
    """Simple keyword-based search in context"""
    query_lower = query.lower()
    lines = context.split('\n')
    
    relevant_sections = []
    current_section = []
    section_header = ""
    
    for line in lines:
        # Track section headers
        if line.startswith('##'):
            if current_section and any(query_lower in l.lower() for l in current_section):
                relevant_sections.append((section_header, current_section))
            section_header = line
            current_section = [line]
        else:
            current_section.append(line)
    
    # Check last section
    if current_section and any(query_lower in l.lower() for l in current_section):
        relevant_sections.append((section_header, current_section))
    
    return relevant_sections


def answer_query(query, context):
    """Generate answer based on query and context"""
    results = search_context(query, context)
    
    if not results:
        return "I don't have specific information about that in my Hyderabad knowledge base. Try asking about food, festivals, travel times, or places to visit!"
    
    answer = f"\n🏙️  Here's what I know about '{query}':\n"
    answer += "=" * 60 + "\n\n"
    
    for header, section in results:
        answer += f"{header}\n"
        for line in section[1:]:  # Skip header line
            if line.strip():
                answer += f"{line}\n"
        answer += "\n"
    
    return answer


def main():
    """Main function to run the Hyderabad assistant"""
    print("=" * 60)
    print("🏛️  Welcome to Hyderabad Culture Assistant!")
    print("=" * 60)
    print("\nLoading Hyderabad context...")
    
    context = load_context()
    print("✓ Context loaded successfully!\n")
    
    print("Ask me anything about Hyderabad!")
    print("Examples:")
    print("  - Suggest famous street food in Hyderabad")
    print("  - Tell me about Hyderabad festivals")
    print("  - Best time to travel in Hyderabad")
    print("\nType 'quit' or 'exit' to stop.\n")
    
    while True:
        try:
            query = input("You: ").strip()
            
            if not query:
                continue
            
            if query.lower() in ['quit', 'exit', 'bye']:
                print("\n👋 Thanks for exploring Hyderabad with me!")
                break
            
            answer = answer_query(query, context)
            print(answer)
            
        except KeyboardInterrupt:
            print("\n\n👋 Thanks for exploring Hyderabad with me!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}\n")


if __name__ == "__main__":
    main()
