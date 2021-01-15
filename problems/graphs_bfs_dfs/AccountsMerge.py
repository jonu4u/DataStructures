# 721. Accounts Merge
# Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.
#
# Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.
#
# After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.
#
# Example 1:
# Input:
# accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
# Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
# Explanation:
# The first and third John's are the same person as they have the common email "johnsmith@mail.com".
# The second John and Mary are different people as none of their email addresses are used by other accounts.
# We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
# ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
# Note:
#
# The length of accounts will be in the range [1, 1000].
# The length of accounts[i] will be in the range [1, 10].
# The length of accounts[i][j] will be in the range [1, 30].
from collections import defaultdict
class Solution(object):

    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        graph = defaultdict(set)
        email_name={}
        # create the graph from account list and also the hashmap where key is email and value is name
        for account in accounts:
            # Each account is a array of name and emails from 2nd element
            name=account[0]
            # if we cut the account list from 2nd element we get list of emails
            # the vertex of graph is the 1st email and the neighbours are the rest emails
            for email in account[1:]:
                first_email=account[1]
                # Add the corresponding element as neighbour to first and first as neighbour to that element
                graph[first_email].add(email)
                graph[email].add(first_email)
                # Add the email name mapping
                email_name[first_email]=name
                email_name[email]=name
            # The above step creates a graph in format {Aemail:(Bemail,Cemail),Bemail:(Cemail,Eemail)} like this
        # Now for each element in graph do dfs, the return list is the connected components merged together,
        # i.e merged accounts
        final_list=[]
        for key in graph.keys():
            # Unless we exhaust the email_name map we do this for each element of graph
            if len(email_name)==0:
                break

            name=email_name.get(key)
            # If the name exists that means the connection is not explored
            if name:
                # Sorted list of emails
                merged_emails=sorted(self.dfs(key,graph))
                # Remove the keys which are in the merged list
                self.remove_keys(email_name,merged_emails)
                final_list.append([name]+merged_emails)
        return final_list


    def dfs(self,root,graph):
        stack=[]
        stack.append(root)
        out_list=[]
        is_visited=set()
        while stack:
            current=stack.pop(0)
            if current not in is_visited:
                is_visited.add(current)
                out_list.append(current)
                neighbors=graph.get(current)
                stack=list(neighbors)+stack
        return out_list

    def remove_keys(self,email_name,remove_list):
        for elem in remove_list:
            if elem in email_name:
                email_name.pop(elem)



s=Solution()
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
print(s.accountsMerge(accounts))