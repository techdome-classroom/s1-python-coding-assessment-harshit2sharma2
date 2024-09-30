def decode_message( s: str, p: str) -> bool:

# write your code here
  
    """
    Determines if a decoder key unlocks a secret message.

    Args:
        s: The secret message.
        p: The decoder key.

    Returns:
        True if the decoder key unlocks the message, False otherwise.
    """

    # Implement the decoding logic here, using the provided information about the wildcard (*) and question mark (?) symbols.
    # You can use a dynamic programming approach or other suitable algorithms.

    # Example implementation:
    if len(s) != len(p):
        return False

    for i in range(len(s)):
        if p[i] != s[i] and p[i] != '*':
            return False

    return True
        return False