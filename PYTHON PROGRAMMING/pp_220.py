# '''
# Exercise 220
# Text Analyzer Using Regular Expressions
# Objective:
# Write a Python program that analyzes a block of text and extracts the following elements using regular expressions:


# Requirements (implement the functions):
# Extract all email addresses from the text.
# Extract all website URLs (both starting with http/https and www).
# Print results to a display.
# Save the results to a text file.

# Expected Output (to display and to file):
# Extracting emails...
# Emails: ['support@example.com', 'john.doe@business.org', 'jane_smith@corporate.net']

# Extracting URLs...
# URLs: ['https://www.example.com', 'http://partner-site.org.', 'www.blogsite.com']

# '''
import re

text = '''
    Dear Team,

    Please reach out to our support team at support@example.com for any assistance. For business inquiries, contact john.doe@business.org or jane_smith@corporate.net.

    You can find more information on our website: https://www.example.com or visit our partner site at http://partner-site.org. Don't forget to check out our blog at www.blogsite.com for the latest updates.

    Best regards,
    The Example Team
    '''


def extract_emails(text: str) -> list[str]:
    """
    Extracts all email addresses from the input text.

    """
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(pattern, text)

    pass


def extract_urls(text: str) -> list[str]:
    """
    Extracts all website URLs from the input text, including those starting with http, https, or www.
    """
    pattern = r'\b(?:https?://|www\.)[a-zA-Z0-9.-]+(?:\.[a-zA-Z]{2,})+/?\S*'
    return re.findall(pattern, text)
    pass


def save_results_to_file(results: list[str], filename: str) -> None:
    """
    Saves the analysis results to a specified text file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        for item in results:
            file.write(f"{item}\n")  # Write each item on a new line

    pass


def print_results_to_display(results: list[str], filename: str) -> None:
    """
    Saves the analysis results to a specified text file.
    """
    print(f"Results saved to {filename}:")
    for item in results:
        print(item)  # Print each item on a new line
    pass


def main():
    # Extract emails and URLs from the text
    emails = extract_emails(text)
    urls = extract_urls(text)

    # Print results to display
    print("Extracting emails...")
    print("Emails:", emails)

    print("\nExtracting URLs...")
    print("URLs:", urls)

    # Save results to a text file
    save_results_to_file(emails, 'emails.txt')
    save_results_to_file(urls, 'urls.txt')

    # Print confirmation of saved results
    print_results_to_display(emails, 'emails.txt')
    print_results_to_display(urls, 'urls.txt')


if __name__ == "__main__":
    main()
# '''
