from graphviz import Digraph

# Create a directed graph
dot = Digraph(format='png', filename='/mnt/data/pleasure_pulse_ERD')

# Users entity
dot.node('Users', '''Users
user_id (PK, AI)
unique_id
email
password_hash
... other attributes''')

# Categories entity
dot.node('Categories', '''Categories
category_id (PK, AI)
category_name
description''')

# Content entity
dot.node('Content', '''Content
content_id (PK, AI)
user_id (FK -> Users)
category_id (FK -> Categories)
title
content_text
image_url
video_url
post_date
is_approved
is_anonymous
is_private''')

# Comments entity
dot.node('Comments', '''Comments
comment_id (PK, AI)
content_id (FK -> Content)
user_id (FK -> Users)
comment_text
comment_date
is_anonymous''')

# Content_Likes entity
dot.node('Content_Likes', '''Content_Likes
like_id (PK, AI)
content_id (FK -> Content)
user_id (FK -> Users)
like_date''')

# User_Follows entity
dot.node('User_Follows', '''User_Follows
follow_id (PK, AI)
follower_id (FK -> Users)
following_id (FK -> Users)
follow_date''')

# Admins entity
dot.node('Admins', '''Admins
admin_id (PK, AI)
user_id (FK -> Users)
role
join_date''')

# Analytics entity
dot.node('Analytics', '''Analytics
analytics_id (PK, AI)
content_id (FK -> Content)
views
comments_count
likes_count
shares_count
report_date''')

# Monetization entity
dot.node('Monetization', '''Monetization
monetization_id (PK, AI)
user_id (FK -> Users)
earnings
payment_method
last_payment_date''')

# User_Reports entity
dot.node('User_Reports', '''User_Reports
report_id (PK, AI)
reporter_id (FK -> Users)
reported_user_id (FK -> Users)
reason
report_date''')

# Content_Reports entity
dot.node('Content_Reports', '''Content_Reports
report_id (PK, AI)
reporter_id (FK -> Users)
content_id (FK -> Content)
reason
report_date''')

# Blocked_Users entity
dot.node('Blocked_Users', '''Blocked_Users
block_id (PK, AI)
blocker_id (FK -> Users)
blocked_user_id (FK -> Users)
block_date''')

# Relationships
dot.edge('Users', 'Content', label='1 -> N')
dot.edge('Users', 'Comments', label='1 -> N')
dot.edge('Users', 'User_Follows', label='1 -> N (Follower/Following)')
dot.edge('Content', 'Categories', label='N -> 1')
dot.edge('Comments', 'Content', label='N -> 1')
dot.edge('Content', 'Users', label='N -> 1')
dot.edge('Content_Likes', 'Content', label='N -> 1')
dot.edge('Content_Likes', 'Users', label='N -> 1')
dot.edge('User_Follows', 'Users', label='N -> 1 (Follower/Following)')
dot.edge('Admins', 'Users', label='N -> 1')
dot.edge('Analytics', 'Content', label='N -> 1')
dot.edge('Monetization', 'Users', label='N -> 1')
dot.edge('User_Reports', 'Users', label='N -> 1 (Reporter/Reported)')
dot.edge('Content_Reports', 'Users', label='N -> 1 (Reporter)')
dot.edge('Content_Reports', 'Content', label='N -> 1')
dot.edge('Blocked_Users', 'Users', label='N -> 1 (Blocker/Blocked)')

# Save the graph to a file
file_path = dot.render()
file_path
