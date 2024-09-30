def decode_message( s: str, p: str) -> bool:

# write your code here
  def can_unlock_message(message, decoder_key):
    m, n = len(message), len(decoder_key)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if message[i - 1] == decoder_key[j - 1] or decoder_key[j - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]
            elif decoder_key[j - 1] == '*':
                for k in range(i):
                    dp[i][j] |= dp[k][j - 1]

    return dp[m][n]

# Test cases
messages = ["aa", "aa", "cb", "abcd", "abcde"]
decoder_keys = ["a", "*", "?a", "*?", "**"]

for message, decoder_key in zip(messages, decoder_keys):
    print(f"Message: {message}, Decoder Key: {decoder_key}, Can Unlock: {can_unlock_message(message, decoder_key)}")
        return False