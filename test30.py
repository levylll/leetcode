class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
        word_dict = {}
        res = []
        word_len = len(words[0])
        all_words = len(words)
        for word in words:
            if word not in word_dict:
                word_dict[word] = 1
            else:
                word_dict[word] += 1

        all_len = all_words * word_len
        start = None
        p = None
        end = None
        for i in range(word_len):
            if p is not None and p == end:
                start = start + word_len
            else:
                start = i
            end = start + all_len
            cur_dict = {}
            p = start
            while p < end and end <= len(s):
                # print('==--=-=-')
                # print(start)
                tmp = s[p:p+word_len]
                if tmp not in word_dict:
                    start = p + word_len
                    end = start + all_len
                    p = start
                    cur_dict = {}
                    continue
                else:
                    if tmp in cur_dict:
                        if cur_dict[tmp] + 1 > word_dict[tmp]:
                            start_tmp = s[start:start+word_len]
                            if start_tmp in cur_dict:
                                if cur_dict[start_tmp] > 1:
                                    cur_dict[start_tmp] -= 1
                                else:
                                    del cur_dict[start_tmp]
                            start += word_len
                            end += word_len
                        else:
                            cur_dict[tmp] += 1
                            p += word_len
                    else:
                        if tmp not in word_dict:
                            start = p + word_len
                            end = start + all_len
                            p = start
                        else:
                            cur_dict[tmp] = 1
                            p += word_len
                if p == end:
                    res.append(start)
                    start += word_len
                    end = start + all_len
                    cur_dict = {}
                    p = start

        return res


# words = "wordgoodgoodgoodbestword"
# s = ["word","good","best","word"]
# s = "barfoothefoobarman"
# words = ["foo","bar"]
# s = "barfoofoobarthefoobarman"
# words = ["bar","foo","the"]
# s = 'lingmindraboofooowingdingbarrwingmonkeypoundcake'
# words = ["fooo","barr","wing","ding","wing"]
s = 'aaa'
words = ['a', 'a']
solution = Solution()
print(solution.findSubstring(s, words))
