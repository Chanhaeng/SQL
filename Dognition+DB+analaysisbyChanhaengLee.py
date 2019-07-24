
# coding: utf-8

# ### Dognition DB Analysis
# Load sql and the database first.
# Then check columns of each table.

# In[2]:


get_ipython().magic('load_ext sql')
get_ipython().magic('sql mysql://studentuser:studentpw@mysqlserver/dognitiondb')
get_ipython().magic('sql USE dognition')


# In[2]:


get_ipython().run_cell_magic('sql', '', 'SHOW tables;')


# In[6]:


get_ipython().run_cell_magic('sql', '', 'SELECT *\nFROM complete_tests\nLIMIT 1;')


# In[7]:


get_ipython().run_cell_magic('sql', '', 'SELECT *\nFROM dogs\nLIMIT 1;')


# In[8]:


get_ipython().run_cell_magic('sql', '', 'SELECT *\nFROM exam_answers\nLIMIT 1;')


# In[13]:


get_ipython().run_cell_magic('sql', '', 'SELECT *\nFROM reviews\nLIMIT 1;')


# In[10]:


get_ipython().run_cell_magic('sql', '', 'SELECT *\nFROM site_activities\nLIMIT 1;')


# In[14]:


get_ipython().run_cell_magic('sql', '', 'SELECT *\nFROM users\nLIMIT 10;')


# # In order to increase the number of complete tests which is the purpose of this analysis, we make the folliwng assumptions.
# 
# ## 1. There are more tests complete in a certain time. 
# 
# ## 2. User in a given area are more active.
# 
# ## 3. Even active users complete tests with low ratings less than other tests.
# 
# ## 4. Fee start user tend to complete less tests. 

# ### I assumed that utc_correction in users table tells you the right local time.
# In that cae, I am going to divide table by morning (6-11a.m.), afternoon (11-5p.m.), night (6-12p.m.), and dawn (12-6a.m. and investigate the number of tests that are completed and divide it by date and month.

# ## 1. First assumption 
# ### divided by morning, afternoon, night, and dawn

# a. When utc_correction applied

# In[103]:


get_ipython().run_cell_magic('sql', '', 'SELECT count(*) AS numtests,\n       (CASE \n        WHEN(TIME(DATE_SUB(c.created_at, INTERVAL ABS(a.utc_correction) HOUR)))<"11:00:00" AND\n        (TIME(DATE_SUB(c.created_at, INTERVAL ABS(a.utc_correction) HOUR)))>"05:59:59" THEN "Morning"\n        \n        WHEN(TIME(DATE_SUB(c.created_at, INTERVAL ABS(a.utc_correction) HOUR)))<"17:00:00" AND\n        (TIME(DATE_SUB(c.created_at, INTERVAL ABS(a.utc_correction) HOUR)))>"10:59:59" THEN "Afternoon"\n       \n        WHEN((TIME(DATE_SUB(c.created_at, INTERVAL ABS(a.utc_correction) HOUR)))<"23:59:59" AND\n        (TIME(DATE_SUB(c.created_at, INTERVAL ABS(a.utc_correction) HOUR)))>"16:59:59")\n        OR \n        (TIME(DATE_SUB(c.created_at, INTERVAL ABS(a.utc_correction) HOUR)))="00:00:00"\n        OR\n        (TIME(DATE_SUB(c.created_at, INTERVAL ABS(a.utc_correction) HOUR)))="23:59:59"\n        THEN "Evening"\n        ELSE "DAWN"\n        END) AS timelabel\nFROM complete_tests c INNER JOIN (SELECT u.utc_correction AS utc_correction, d.dog_guid AS dog_guid\n                                FROM dogs d INNER JOIN users u\n                                    ON d.user_guid=u.user_guid\n                                WHERE (d.exclude=0 OR d.exclude IS NULL) AND (u.exclude=0 OR u.exclude IS NULL)\n                                 AND u.utc_correction<0) a\n    ON c.dog_guid=a.dog_guid\nGROUP BY timelabel\nORDER BY numtests DESC;')


# b. when utc_correction not applied

# In[91]:


get_ipython().run_cell_magic('sql', '', 'SELECT TIME(c.created_at) AS time, count(*) AS numtests,\n       (CASE \n        WHEN TIME(c.created_at)<"11:00:00" AND\n        TIME(c.created_at)>"05:59:59" THEN "Morning"\n        \n        WHEN TIME(c.created_at)<"17:00:00" AND\n        TIME(c.created_at)>"10:59:59" THEN "Afternoon"\n       \n        WHEN (TIME(c.created_at)<"23:59:59" AND\n        TIME(c.created_at)>"16:59:59")\n        OR \n        TIME(c.created_at)="00:00:00"\n        OR\n        TIME(c.created_at)="23:59:59"\n        THEN "Evening"\n        \n        WHEN TIME(c.created_at)<"06:00:00" AND\n        TIME(c.created_at)>"00:00:00" THEN "DAWN"\n        END) AS timelabel\n    \nFROM complete_tests c INNER JOIN (SELECT d.dog_guid AS dog_guid\n                                FROM dogs d INNER JOIN users u\n                                    ON d.user_guid=u.user_guid\n                                WHERE (d.exclude=0 OR d.exclude IS NULL) AND (u.exclude=0 OR u.exclude IS NULL)\n                                 AND u.utc_correction<0) a\n    ON c.dog_guid=a.dog_guid\nGROUP BY timelabel\nORDER BY numtests DESC;')


# ### There are a big difference between a and b (whether utc_correction is applied or not). 
# 
# When it is not applied, over 86% of the total complete tests are performed(tested) during night or dawn time, which rarely happen. 
# 
# When it is applied, there is a tendency found that people do the tests during afternoon or night time compared to morning time.

# Then we are going to take a look by date.

# In[109]:


get_ipython().run_cell_magic('sql', '', 'SELECT DAYOFWEEK(DATE_SUB(c.created_at, INTERVAL ABS(a.utc_correction) HOUR)) AS day, count(*) AS numtests,\n       (CASE\n        WHEN DAYOFWEEK(DATE_SUB(c.created_at, INTERVAL ABS(a.utc_correction) HOUR))=1 THEN "Su"\n        WHEN DAYOFWEEK(DATE_SUB(c.created_at, INTERVAL ABS(a.utc_correction) HOUR))=2 THEN "Mo"\n        WHEN DAYOFWEEK(DATE_SUB(c.created_at, INTERVAL ABS(a.utc_correction) HOUR))=3 THEN "Tu"\n        WHEN DAYOFWEEK(DATE_SUB(c.created_at, INTERVAL ABS(a.utc_correction) HOUR))=4 THEN "We"\n        WHEN DAYOFWEEK(DATE_SUB(c.created_at, INTERVAL ABS(a.utc_correction) HOUR))=5 THEN "Th"\n        WHEN DAYOFWEEK(DATE_SUB(c.created_at, INTERVAL ABS(a.utc_correction) HOUR))=6 THEN "Fr"\n        WHEN DAYOFWEEK(DATE_SUB(c.created_at, INTERVAL ABS(a.utc_correction) HOUR))=7 THEN "Sa"\n        END) AS daylabel\nFROM complete_tests c INNER JOIN (SELECT u.utc_correction AS utc_correction, d.dog_guid AS dog_guid\n                                FROM dogs d INNER JOIN users u\n                                    ON d.user_guid=u.user_guid\n                                WHERE (d.exclude=0 OR d.exclude IS NULL) AND (u.exclude=0 OR u.exclude IS NULL)\n                                 AND u.utc_correction<0) a\n    ON c.dog_guid=a.dog_guid\nGROUP BY daylabel\nORDER BY numtests DESC;')


# In[105]:


get_ipython().run_cell_magic('sql', '', 'SELECT DAYOFWEEK(c.created_at), COUNT(c.created_at) AS numtests,\n(CASE\nWHEN DAYOFWEEK(c.created_at)=1 THEN "Su"\nWHEN DAYOFWEEK(c.created_at)=2 THEN "Mo"\nWHEN DAYOFWEEK(c.created_at)=3 THEN "Tu"\nWHEN DAYOFWEEK(c.created_at)=4 THEN "We"\nWHEN DAYOFWEEK(c.created_at)=5 THEN "Th"\nWHEN DAYOFWEEK(c.created_at)=6 THEN "Fr"\nWHEN DAYOFWEEK(c.created_at)=7 THEN "Sa"\nEND) AS daylabel\nFROM complete_tests c JOIN dogs d\nON c.dog_guid=d.dog_guid\nWHERE d.exclude IS NULL OR d.exclude=0\nGROUP BY daylabel\nORDER BY numtests DESC;')


# No matther whether utc_correction is applied or not, the results are the same. 
# 
# We are going to investigate it by date and time.

# In[115]:


get_ipython().run_cell_magic('sql', '', 'SELECT  count(*) AS numtests,\n       (CASE \n        WHEN(TIME(DATE_SUB(c.created_at, INTERVAL ABS(a.utc_correction) HOUR)))<"11:00:00" AND\n        (TIME(DATE_SUB(c.created_at, INTERVAL ABS(a.utc_correction) HOUR)))>"05:59:59" THEN "Morning"\n        \n        WHEN(TIME(DATE_SUB(c.created_at, INTERVAL ABS(a.utc_correction) HOUR)))<"17:00:00" AND\n        (TIME(DATE_SUB(c.created_at, INTERVAL ABS(a.utc_correction) HOUR)))>"10:59:59" THEN "Afternoon"\n       \n        WHEN((TIME(DATE_SUB(c.created_at, INTERVAL ABS(a.utc_correction) HOUR)))<"23:59:59" AND\n        (TIME(DATE_SUB(c.created_at, INTERVAL ABS(a.utc_correction) HOUR)))>"16:59:59")\n        OR \n        (TIME(DATE_SUB(c.created_at, INTERVAL ABS(a.utc_correction) HOUR)))="00:00:00"\n        OR\n        (TIME(DATE_SUB(c.created_at, INTERVAL ABS(a.utc_correction) HOUR)))="23:59:59"\n        THEN "Evening"\n        ELSE "DAWN"\n        END) AS timelabel,\n        DAYOFWEEK(DATE_SUB(c.created_at, INTERVAL ABS(a.utc_correction) HOUR)) AS day,\n        (CASE\n        WHEN DAYOFWEEK(DATE_SUB(c.created_at, INTERVAL ABS(a.utc_correction) HOUR))=1 THEN "Su"\n        WHEN DAYOFWEEK(DATE_SUB(c.created_at, INTERVAL ABS(a.utc_correction) HOUR))=2 THEN "Mo"\n        WHEN DAYOFWEEK(DATE_SUB(c.created_at, INTERVAL ABS(a.utc_correction) HOUR))=3 THEN "Tu"\n        WHEN DAYOFWEEK(DATE_SUB(c.created_at, INTERVAL ABS(a.utc_correction) HOUR))=4 THEN "We"\n        WHEN DAYOFWEEK(DATE_SUB(c.created_at, INTERVAL ABS(a.utc_correction) HOUR))=5 THEN "Th"\n        WHEN DAYOFWEEK(DATE_SUB(c.created_at, INTERVAL ABS(a.utc_correction) HOUR))=6 THEN "Fr"\n        WHEN DAYOFWEEK(DATE_SUB(c.created_at, INTERVAL ABS(a.utc_correction) HOUR))=7 THEN "Sa"\n        END) AS daylabel\n\nFROM complete_tests c INNER JOIN (SELECT u.utc_correction AS utc_correction, d.dog_guid AS dog_guid\n                                FROM dogs d INNER JOIN users u\n                                    ON d.user_guid=u.user_guid\n                                WHERE (d.exclude=0 OR d.exclude IS NULL) AND (u.exclude=0 OR u.exclude IS NULL)\n                                 AND u.utc_correction<0) a\n    ON c.dog_guid=a.dog_guid\nGROUP BY daylabel, timelabel\nORDER BY numtests DESC;')


# ### As the table above suggests, we know that people do more tests on a certain date and during a certian period of time

# ## 2. Second assumption
# 
# #### Now we are going to investigate our second assumption, which is "user in a given area are more active".

# In[125]:


get_ipython().run_cell_magic('sql', '', 'SELECT count(*) AS totaltests, count(*)/count(DISTINCT a.user_guid) AS avg\nFROM complete_tests c INNER JOIN (SELECT d.dog_guid AS dog_guid, u.user_guid AS user_guid\n                                FROM dogs d INNER JOIN users u\n                                    ON d.user_guid=u.user_guid\n                                WHERE (d.exclude=0 OR d.exclude IS NULL) AND (u.exclude=0 OR u.exclude IS NULL)\n                                ) a\n    ON  c.dog_guid=a.dog_guid;')


# In[137]:


get_ipython().run_cell_magic('sql', '', 'SELECT a.country AS country, count(*) AS totaltests, COUNT(DISTINCT a.user_guid) AS numusers,\n        count(*)/count(DISTINCT a.user_guid) AS avg\nFROM complete_tests c INNER JOIN (SELECT d.dog_guid AS dog_guid, u.user_guid AS user_guid,\n                                  u.state AS state, u.country As country\n                                FROM dogs d INNER JOIN users u\n                                    ON d.user_guid=u.user_guid\n                                WHERE (d.exclude=0 OR d.exclude IS NULL) AND (u.exclude=0 OR u.exclude IS NULL)\n                                ) a\n    ON  c.dog_guid=a.dog_guid\nGROUP BY a.country\nORDER BY totaltests DESC;')


# In[138]:


get_ipython().run_cell_magic('sql', '', 'SELECT a.country AS country, count(*) AS totaltests, COUNT(DISTINCT a.user_guid) AS numusers,\n        count(*)/count(DISTINCT a.user_guid) AS avg\nFROM complete_tests c INNER JOIN (SELECT d.dog_guid AS dog_guid, u.user_guid AS user_guid,\n                                  u.state AS state, u.country As country\n                                FROM dogs d INNER JOIN users u\n                                    ON d.user_guid=u.user_guid\n                                WHERE (d.exclude=0 OR d.exclude IS NULL) AND (u.exclude=0 OR u.exclude IS NULL)\n                                ) a\n    ON  c.dog_guid=a.dog_guid\nGROUP BY a.country\nORDER BY avg DESC;')


# We have the far larger number of American users than other countires. For Hungry, even though there average number of complete tests are the largest, we only have 4 users. 
# 
# We are going to look at data according to American states.

# In[26]:


get_ipython().run_cell_magic('sql', '', 'SELECT a.state AS state, count(*) AS totaltests, COUNT(DISTINCT a.user_guid) AS numusers,\n        count(*)/count(DISTINCT a.user_guid) AS avg\nFROM complete_tests c INNER JOIN (SELECT d.dog_guid AS dog_guid, u.user_guid AS user_guid,\n                                  u.state AS state, u.country As country\n                                FROM dogs d INNER JOIN users u\n                                    ON d.user_guid=u.user_guid\n                                WHERE (d.exclude=0 OR d.exclude IS NULL) AND (u.exclude=0 OR u.exclude IS NULL)\n                                ) a\n    ON  c.dog_guid=a.dog_guid\nWHERE a.country="US"\nGROUP BY state\nORDER BY numusers DESC\nLIMIT 10;')


# In[146]:


get_ipython().run_cell_magic('sql', '', 'SELECT a.state AS state, count(*) AS totaltests, COUNT(DISTINCT a.user_guid) AS numusers,\n        count(*)/count(DISTINCT a.user_guid) AS avg\nFROM complete_tests c INNER JOIN (SELECT d.dog_guid AS dog_guid, u.user_guid AS user_guid,\n                                  u.state AS state, u.country As country\n                                FROM dogs d INNER JOIN users u\n                                    ON d.user_guid=u.user_guid\n                                WHERE (d.exclude=0 OR d.exclude IS NULL) AND (u.exclude=0 OR u.exclude IS NULL)\n                                ) a\n    ON  c.dog_guid=a.dog_guid\nWHERE a.country="US"\nGROUP BY state\nORDER BY avg DESC\nLIMIT 10;')


# When we look at the average and the number of users, NC and VA are the only states that are in the top 10 according to the both criteria.

# ## 3. The thrid assumption
# #### Even active users complete tests with low ratings less than other tests.

# In[18]:


get_ipython().run_cell_magic('sql', '', 'SELECT DISTINCT test_name AS test, AVG(rating) as avgrating\nFROM reviews\nWHERE rating IS NOT NULL\nGROUP BY test\nLIMIT 10;')


# What is the average of the total?

# In[20]:


get_ipython().run_cell_magic('sql', '', 'SELECT AVG(rating) as avgrating\nFROM reviews\nWHERE rating IS NOT NULL;')


# Let;s look at the tests whose average is lower thatn the average of the total

# In[32]:


get_ipython().run_cell_magic('sql', '', 'SELECT DISTINCT test_name AS test, AVG(rating) as avgrating, subcategory_name\nFROM reviews\nWHERE rating IS NOT NULL\nGROUP BY test\nHAVING avgrating<2.6980\n;')


# Let's see how many users do the tests

# In[33]:


get_ipython().run_cell_magic('sql', '', 'SELECT DISTINCT test_name AS test, AVG(rating) as avgrating, subcategory_name, COUNT(DISTINCT user_guid) AS numusers\nFROM reviews\nWHERE rating IS NOT NULL\nGROUP BY test\nHAVING avgrating<2.6980\n;')


# According to test, what is the number of users who rated?

# In[37]:


get_ipython().run_cell_magic('sql', '', 'SELECT DISTINCT test_name AS test, (COUNT(DISTINCT user_guid)) as numusers\nFROM reviews\nWHERE rating IS NOT NULL\nGROUP BY test\nLIMIT 10;')


# There is a huge gap(variance) in the number of users who rated.

# In[47]:


get_ipython().run_cell_magic('sql', '', 'SELECT AVG(a.numusers) AS avg\nFROM (SELECT DISTINCT test_name AS test, (COUNT(DISTINCT user_guid)) as numusers\n        FROM reviews\n        WHERE rating IS NOT NULL\n        GROUP BY test) a\n;')


# The number of tests done by a user.

# In[62]:


get_ipython().run_cell_magic('sql', '', 'SELECT DISTINCT user_guid as user, COUNT(test_name) AS numtests\nFROM reviews\nGROUP BY user\nORDER BY numtests DESC\nLIMIT 10;')


# There are not many users who did not rate compared the number of users.

# In[67]:


get_ipython().run_cell_magic('sql', '', 'SELECT AVG(a.numtests)\nFROM(SELECT DISTINCT user_guid as user, COUNT(test_name) AS numtests\n    FROM reviews\n    GROUP BY user) a\n;')


# The average of the number of complete tests is about 5.5. 
# We are going to look how is the ratings to a test that assessed by users with a higher number of compltest tests.

# 평균 한 유저당 푸는 테스트 수는 약 5.5개 정도이다. 그렇다면 평균보다 높은 문제를 푸는 유저들이 가진 리뷰 평균은 비슷할까

# In[83]:


get_ipython().run_cell_magic('sql', '', 'SELECT DISTINCT test_name AS test, AVG(rating) AS avgrating\nFROM reviews r INNER JOIN (SELECT DISTINCT user_guid as user, COUNT(test_name) AS numtests \n                           FROM reviews\n                           GROUP BY user\n                           HAVING numtests > 5.49) a\n    ON r.user_guid=a.user\nGROUP BY test\nORDER BY avgrating DESC\nLIMIT 10;')


# In[82]:


get_ipython().run_cell_magic('sql', '', 'SELECT DISTINCT test_name AS test, AVG(rating) as avgrating\nFROM reviews\nWHERE rating IS NOT NULL\nGROUP BY test\nORDER BY avgrating DESC\nLIMIT 10;')


# ### The fourth assumption
# 
# #### 4. Fee start user tend to complete less tests.

# First, we are going to calculate the number of complete tests by a users. 
# 
# Like we saw before, the number of tests without rating is less than 10% of the total. (Complete_tests table is used for accuracy).

# In[98]:


get_ipython().run_cell_magic('sql', '', 'SELECT DISTINCT a.user_guid AS users, COUNT(*) AS numtest\nFROM complete_tests c INNER JOIN (SELECT d.dog_guid AS dog_guid, u.user_guid AS user_guid\n                                FROM dogs d INNER JOIN users u\n                                    ON d.user_guid=u.user_guid\n                                WHERE (d.exclude=0 OR d.exclude IS NULL) AND (u.exclude=0 OR u.exclude IS NULL)\n                                 ) a\n    ON c.dog_guid=a.dog_guid\nGROUP BY users\nORDER BY numtest DESC\n;')


# Then how is the average by free start users?

# In[107]:


get_ipython().run_cell_magic('sql', '', 'SELECT distinct free_start_user as free, count(*) AS count\nFROM users\nGROUP BY free;')


# Free_start_user is indicated by None, 0 and 1. 
# Let's assums that 1 is the one who started free.

# In[108]:


get_ipython().run_cell_magic('sql', '', 'SELECT DISTINCT a.user_guid AS users, COUNT(*) AS numtest\nFROM complete_tests c INNER JOIN (SELECT d.dog_guid AS dog_guid, u.user_guid AS user_guid\n                                FROM dogs d INNER JOIN users u\n                                    ON d.user_guid=u.user_guid\n                                WHERE (d.exclude=0 OR d.exclude IS NULL) AND (u.exclude=0 OR u.exclude IS NULL)\n                                 AND u.free_start_user=1) a\n    ON c.dog_guid=a.dog_guid\nGROUP BY users\nORDER BY numtest DESC\n;')


# In[110]:


get_ipython().run_cell_magic('sql', '', 'SELECT AVG(a.numtest) AS AVG\nFROM (SELECT DISTINCT a.user_guid AS users, COUNT(*) AS numtest\nFROM complete_tests c INNER JOIN (SELECT d.dog_guid AS dog_guid, u.user_guid AS user_guid\n                                FROM dogs d INNER JOIN users u\n                                    ON d.user_guid=u.user_guid\n                                WHERE (d.exclude=0 OR d.exclude IS NULL) AND (u.exclude=0 OR u.exclude IS NULL)\n                                 AND u.free_start_user=1) a\n    ON c.dog_guid=a.dog_guid\nGROUP BY users) a\n;')


# The average of users who is not free_start_users.

# In[112]:


get_ipython().run_cell_magic('sql', '', 'SELECT DISTINCT a.user_guid AS users, COUNT(*) AS numtest\nFROM complete_tests c INNER JOIN (SELECT d.dog_guid AS dog_guid, u.user_guid AS user_guid\n                                FROM dogs d INNER JOIN users u\n                                    ON d.user_guid=u.user_guid\n                                WHERE (d.exclude=0 OR d.exclude IS NULL) AND (u.exclude=0 OR u.exclude IS NULL)\n                                 AND ((u.free_start_user IS NULL) OR (u.free_start_user=0))) a\n    ON c.dog_guid=a.dog_guid\nGROUP BY users\nORDER BY numtest DESC\n;')


# User whose id is "ce7b75bc-7144-11e5-ba71-058fbc01cf0b" completed too many tests compared to the others (considered as an outlier).

# In[114]:


get_ipython().run_cell_magic('sql', '', 'SELECT AVG(a.numtest) AS AVG\nFROM (SELECT DISTINCT a.user_guid AS users, COUNT(*) AS numtest\nFROM complete_tests c INNER JOIN (SELECT d.dog_guid AS dog_guid, u.user_guid AS user_guid\n                                FROM dogs d INNER JOIN users u\n                                    ON d.user_guid=u.user_guid\n                                WHERE (d.exclude=0 OR d.exclude IS NULL) AND (u.exclude=0 OR u.exclude IS NULL)\n                                 AND ((u.free_start_user IS NULL) OR (u.free_start_user=0)) ) a\n    ON c.dog_guid=a.dog_guid\nGROUP BY users\nHAVING a.user_guid !="ce7b75bc-7144-11e5-ba71-058fbc01cf0b") a\n;')


# The average of users who is not free_start_users is far larger than who is a free_start_users.

# In[ ]:




