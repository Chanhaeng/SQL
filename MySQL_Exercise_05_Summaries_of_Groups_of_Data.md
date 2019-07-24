
Copyright Jana Schaich Borg/Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)

# MySQL Exercise 5: Summaries of Groups of Data

So far you've learned how to select, reformat, manipulate, order, and summarize data from a single table in database.  In this lesson, you are going to learn how to summarize multiple subsets of your data in the same query.  The method for doing this is to include a "GROUP BY" clause in your SQL query.  
  
    

## The GROUP BY clause

The GROUP BY clause comes after the WHERE clause, but before ORDER BY or LIMIT:

<img src="https://duke.box.com/shared/static/lc0yjfz1339q3mc04ne13m2q5tkzy3x7.jpg" width=400 alt="SELECT FROM WHERE ORDER BY" />

The GROUP BY clause is easy to incorporate into your queries.  In fact, it might be a little too easy to incorporate into MySQL queries, because it can be used incorrectly in MySQL queries even when no error message is displayed.  As a consequence, I suggest you adopt a healthy dose of caution every time you use the GROUP BY clause.  By the end of this lesson, you will understand why.  When used correctly, though, GROUP BY is one of the most useful and efficient parts of an SQL query, and once you are comfortable using it, you will use it very frequently.

**To get started, load the SQL library and the Dognition database, and set the dognition database as the default:**



```python
%load_ext sql
%sql mysql://studentuser:studentpw@mysqlserver/dognitiondb
%sql USE dognitiondb
```

    0 rows affected.





    []



Let's return to a question from MySQL Exercise 4.  How would you query the average rating for each of the 40 tests in the Reviews table? As we discussed, one very inefficient method to do that would be to write 40 separate queries with each one having a different test name in the WHERE conditional clause.  Then you could copy or transcribe the results from all 40 queries into one place.  But that wouldn't be very pleasant.  Here's how you could do the same thing using one query that has a GROUP BY clause:

```mySQL
SELECT test_name, AVG(rating) AS AVG_Rating
FROM reviews
GROUP BY test_name
```

This query will output the average rating for each test.  More technically, this query will instruct MySQL to average all the rows that have the same value in the test_name column.

Notice that I included test_name in the SELECT statement.  As a strong rule of thumb, if you are grouping by a column, you should also include that column in the SELECT statement.  If you don't do this, you won't know to which group each row of your output corresponds.  
     
**To see what I mean, try the query above without test_name included in the SELECT statement:**


```python
%%sql
SELECT test_name, AVG(rating) AS AVG_Rating
FROM reviews
GROUP BY test_name;
```

    40 rows affected.





<table>
    <tr>
        <th>test_name</th>
        <th>AVG_Rating</th>
    </tr>
    <tr>
        <td>1 vs 1 Game</td>
        <td>3.9206</td>
    </tr>
    <tr>
        <td>3 vs 1 Game</td>
        <td>4.2857</td>
    </tr>
    <tr>
        <td>5 vs 1 Game</td>
        <td>3.9272</td>
    </tr>
    <tr>
        <td>Arm Pointing</td>
        <td>4.2153</td>
    </tr>
    <tr>
        <td>Cover Your Eyes</td>
        <td>2.6741</td>
    </tr>
    <tr>
        <td>Delayed Cup Game</td>
        <td>3.3514</td>
    </tr>
    <tr>
        <td>Different Perspective</td>
        <td>2.7647</td>
    </tr>
    <tr>
        <td>Expression Game</td>
        <td>4.0000</td>
    </tr>
    <tr>
        <td>Eye Contact Game</td>
        <td>2.9372</td>
    </tr>
    <tr>
        <td>Eye Contact Warm-up</td>
        <td>0.9632</td>
    </tr>
    <tr>
        <td>Foot Pointing</td>
        <td>4.0093</td>
    </tr>
    <tr>
        <td>Impossible Task Game</td>
        <td>3.0965</td>
    </tr>
    <tr>
        <td>Impossible Task Warm-up</td>
        <td>0.2174</td>
    </tr>
    <tr>
        <td>Inferential Reasoning Game</td>
        <td>4.5223</td>
    </tr>
    <tr>
        <td>Inferential Reasoning Warm-up</td>
        <td>4.3066</td>
    </tr>
    <tr>
        <td>Memory versus Pointing</td>
        <td>3.5584</td>
    </tr>
    <tr>
        <td>Memory versus Smell</td>
        <td>4.2623</td>
    </tr>
    <tr>
        <td>Navigation Game</td>
        <td>2.9841</td>
    </tr>
    <tr>
        <td>Navigation Learning</td>
        <td>2.0303</td>
    </tr>
    <tr>
        <td>Navigation Warm-up</td>
        <td>1.9805</td>
    </tr>
    <tr>
        <td>Numerosity Warm-Up</td>
        <td>2.6173</td>
    </tr>
    <tr>
        <td>One Cup Warm-up</td>
        <td>1.3693</td>
    </tr>
    <tr>
        <td>Physical Reasoning Game</td>
        <td>3.8492</td>
    </tr>
    <tr>
        <td>Physical Reasoning Warm-up</td>
        <td>1.6625</td>
    </tr>
    <tr>
        <td>Self Control Game</td>
        <td>3.8519</td>
    </tr>
    <tr>
        <td>Shaker Game</td>
        <td>4.6667</td>
    </tr>
    <tr>
        <td>Shaker Warm-Up</td>
        <td>2.1818</td>
    </tr>
    <tr>
        <td>Shared Perspective</td>
        <td>3.2778</td>
    </tr>
    <tr>
        <td>Slide</td>
        <td>4.5111</td>
    </tr>
    <tr>
        <td>Smell Game</td>
        <td>4.2857</td>
    </tr>
    <tr>
        <td>Stair Game</td>
        <td>4.2857</td>
    </tr>
    <tr>
        <td>Switch</td>
        <td>5.5676</td>
    </tr>
    <tr>
        <td>Treat Warm-up</td>
        <td>0.7909</td>
    </tr>
    <tr>
        <td>Turn Your Back</td>
        <td>3.1293</td>
    </tr>
    <tr>
        <td>Two Cup Warm-up</td>
        <td>1.6737</td>
    </tr>
    <tr>
        <td>Warm-Up</td>
        <td>1.2020</td>
    </tr>
    <tr>
        <td>Watching</td>
        <td>2.4594</td>
    </tr>
    <tr>
        <td>Watching - Part 2</td>
        <td>2.6570</td>
    </tr>
    <tr>
        <td>Yawn Game</td>
        <td>2.8477</td>
    </tr>
    <tr>
        <td>Yawn Warm-up</td>
        <td>2.0035</td>
    </tr>
</table>



You can form groups using derived values as well as original columns.  To illustrate this, let's address another question: how many tests were completed during each month of the year?

To answer this question, we need to take advantage of another datetime function described in the website below:

http://www.w3resource.com/mysql/date-and-time-functions/date-and-time-functions.php

MONTH() will return a number representing the month of a date entry. To get the total number of tests completed each month, you could put the MONTH function into the GROUP BY clause, in this case through an alias:

```mySQL
SELECT test_name, MONTH(created_at) AS Month, COUNT(created_at) AS Num_Completed_Tests
FROM complete_tests
GROUP BY Month;
```

You can also group by multiple columns or derived fields.  If we wanted to determine the total number of each type of test completed each month, you could include both "test_name" and the derived "Month" field in the GROUP BY clause, separated by a comma.

```mySQL
SELECT test_name, MONTH(created_at) AS Month, COUNT(created_at) AS Num_Completed_Tests
FROM complete_tests
GROUP BY test_name, Month;
```

MySQL allows you to use aliases in a GROUP BY clause, but some database systems do not.  If you are using a database system that does NOT accept aliases in GROUP BY clauses, you can still group by derived fields, but you have to duplicate the calculation for the derived field in the GROUP BY clause in addition to including the derived field in the SELECT clause:

```mySQL
SELECT test_name, MONTH(created_at) AS Month, COUNT(created_at) AS Num_Completed_Tests
FROM complete_tests
GROUP BY test_name, MONTH(created_at);
```  
  
Try the query once with test_name first in the GROUP BY list, and once with Month first in the GROUP BY list below.  Inspect the outputs:


```python
%%sql
SELECT test_name, MONTH(created_at) AS Month, COUNT(created_at) AS Num_Completed_Tests
FROM complete_tests
GROUP BY test_name, MONTH;
```

    480 rows affected.





<table>
    <tr>
        <th>test_name</th>
        <th>Month</th>
        <th>Num_Completed_Tests</th>
    </tr>
    <tr>
        <td>1 vs 1 Game</td>
        <td>1</td>
        <td>25</td>
    </tr>
    <tr>
        <td>1 vs 1 Game</td>
        <td>2</td>
        <td>28</td>
    </tr>
    <tr>
        <td>1 vs 1 Game</td>
        <td>3</td>
        <td>22</td>
    </tr>
    <tr>
        <td>1 vs 1 Game</td>
        <td>4</td>
        <td>12</td>
    </tr>
    <tr>
        <td>1 vs 1 Game</td>
        <td>5</td>
        <td>13</td>
    </tr>
    <tr>
        <td>1 vs 1 Game</td>
        <td>6</td>
        <td>18</td>
    </tr>
    <tr>
        <td>1 vs 1 Game</td>
        <td>7</td>
        <td>36</td>
    </tr>
    <tr>
        <td>1 vs 1 Game</td>
        <td>8</td>
        <td>17</td>
    </tr>
    <tr>
        <td>1 vs 1 Game</td>
        <td>9</td>
        <td>28</td>
    </tr>
    <tr>
        <td>1 vs 1 Game</td>
        <td>10</td>
        <td>27</td>
    </tr>
    <tr>
        <td>1 vs 1 Game</td>
        <td>11</td>
        <td>15</td>
    </tr>
    <tr>
        <td>1 vs 1 Game</td>
        <td>12</td>
        <td>14</td>
    </tr>
    <tr>
        <td>3 vs 1 Game</td>
        <td>1</td>
        <td>35</td>
    </tr>
    <tr>
        <td>3 vs 1 Game</td>
        <td>2</td>
        <td>28</td>
    </tr>
    <tr>
        <td>3 vs 1 Game</td>
        <td>3</td>
        <td>34</td>
    </tr>
    <tr>
        <td>3 vs 1 Game</td>
        <td>4</td>
        <td>16</td>
    </tr>
    <tr>
        <td>3 vs 1 Game</td>
        <td>5</td>
        <td>34</td>
    </tr>
    <tr>
        <td>3 vs 1 Game</td>
        <td>6</td>
        <td>42</td>
    </tr>
    <tr>
        <td>3 vs 1 Game</td>
        <td>7</td>
        <td>37</td>
    </tr>
    <tr>
        <td>3 vs 1 Game</td>
        <td>8</td>
        <td>23</td>
    </tr>
    <tr>
        <td>3 vs 1 Game</td>
        <td>9</td>
        <td>24</td>
    </tr>
    <tr>
        <td>3 vs 1 Game</td>
        <td>10</td>
        <td>28</td>
    </tr>
    <tr>
        <td>3 vs 1 Game</td>
        <td>11</td>
        <td>22</td>
    </tr>
    <tr>
        <td>3 vs 1 Game</td>
        <td>12</td>
        <td>45</td>
    </tr>
    <tr>
        <td>5 vs 1 Game</td>
        <td>1</td>
        <td>59</td>
    </tr>
    <tr>
        <td>5 vs 1 Game</td>
        <td>2</td>
        <td>54</td>
    </tr>
    <tr>
        <td>5 vs 1 Game</td>
        <td>3</td>
        <td>57</td>
    </tr>
    <tr>
        <td>5 vs 1 Game</td>
        <td>4</td>
        <td>29</td>
    </tr>
    <tr>
        <td>5 vs 1 Game</td>
        <td>5</td>
        <td>50</td>
    </tr>
    <tr>
        <td>5 vs 1 Game</td>
        <td>6</td>
        <td>61</td>
    </tr>
    <tr>
        <td>5 vs 1 Game</td>
        <td>7</td>
        <td>69</td>
    </tr>
    <tr>
        <td>5 vs 1 Game</td>
        <td>8</td>
        <td>38</td>
    </tr>
    <tr>
        <td>5 vs 1 Game</td>
        <td>9</td>
        <td>50</td>
    </tr>
    <tr>
        <td>5 vs 1 Game</td>
        <td>10</td>
        <td>54</td>
    </tr>
    <tr>
        <td>5 vs 1 Game</td>
        <td>11</td>
        <td>40</td>
    </tr>
    <tr>
        <td>5 vs 1 Game</td>
        <td>12</td>
        <td>59</td>
    </tr>
    <tr>
        <td>Arm Pointing</td>
        <td>1</td>
        <td>622</td>
    </tr>
    <tr>
        <td>Arm Pointing</td>
        <td>2</td>
        <td>498</td>
    </tr>
    <tr>
        <td>Arm Pointing</td>
        <td>3</td>
        <td>507</td>
    </tr>
    <tr>
        <td>Arm Pointing</td>
        <td>4</td>
        <td>381</td>
    </tr>
    <tr>
        <td>Arm Pointing</td>
        <td>5</td>
        <td>1149</td>
    </tr>
    <tr>
        <td>Arm Pointing</td>
        <td>6</td>
        <td>1424</td>
    </tr>
    <tr>
        <td>Arm Pointing</td>
        <td>7</td>
        <td>913</td>
    </tr>
    <tr>
        <td>Arm Pointing</td>
        <td>8</td>
        <td>779</td>
    </tr>
    <tr>
        <td>Arm Pointing</td>
        <td>9</td>
        <td>1243</td>
    </tr>
    <tr>
        <td>Arm Pointing</td>
        <td>10</td>
        <td>2535</td>
    </tr>
    <tr>
        <td>Arm Pointing</td>
        <td>11</td>
        <td>735</td>
    </tr>
    <tr>
        <td>Arm Pointing</td>
        <td>12</td>
        <td>666</td>
    </tr>
    <tr>
        <td>Cover Your Eyes</td>
        <td>1</td>
        <td>452</td>
    </tr>
    <tr>
        <td>Cover Your Eyes</td>
        <td>2</td>
        <td>373</td>
    </tr>
    <tr>
        <td>Cover Your Eyes</td>
        <td>3</td>
        <td>416</td>
    </tr>
    <tr>
        <td>Cover Your Eyes</td>
        <td>4</td>
        <td>291</td>
    </tr>
    <tr>
        <td>Cover Your Eyes</td>
        <td>5</td>
        <td>753</td>
    </tr>
    <tr>
        <td>Cover Your Eyes</td>
        <td>6</td>
        <td>767</td>
    </tr>
    <tr>
        <td>Cover Your Eyes</td>
        <td>7</td>
        <td>521</td>
    </tr>
    <tr>
        <td>Cover Your Eyes</td>
        <td>8</td>
        <td>408</td>
    </tr>
    <tr>
        <td>Cover Your Eyes</td>
        <td>9</td>
        <td>574</td>
    </tr>
    <tr>
        <td>Cover Your Eyes</td>
        <td>10</td>
        <td>1653</td>
    </tr>
    <tr>
        <td>Cover Your Eyes</td>
        <td>11</td>
        <td>595</td>
    </tr>
    <tr>
        <td>Cover Your Eyes</td>
        <td>12</td>
        <td>447</td>
    </tr>
    <tr>
        <td>Delayed Cup Game</td>
        <td>1</td>
        <td>356</td>
    </tr>
    <tr>
        <td>Delayed Cup Game</td>
        <td>2</td>
        <td>319</td>
    </tr>
    <tr>
        <td>Delayed Cup Game</td>
        <td>3</td>
        <td>350</td>
    </tr>
    <tr>
        <td>Delayed Cup Game</td>
        <td>4</td>
        <td>256</td>
    </tr>
    <tr>
        <td>Delayed Cup Game</td>
        <td>5</td>
        <td>539</td>
    </tr>
    <tr>
        <td>Delayed Cup Game</td>
        <td>6</td>
        <td>525</td>
    </tr>
    <tr>
        <td>Delayed Cup Game</td>
        <td>7</td>
        <td>407</td>
    </tr>
    <tr>
        <td>Delayed Cup Game</td>
        <td>8</td>
        <td>355</td>
    </tr>
    <tr>
        <td>Delayed Cup Game</td>
        <td>9</td>
        <td>424</td>
    </tr>
    <tr>
        <td>Delayed Cup Game</td>
        <td>10</td>
        <td>1019</td>
    </tr>
    <tr>
        <td>Delayed Cup Game</td>
        <td>11</td>
        <td>422</td>
    </tr>
    <tr>
        <td>Delayed Cup Game</td>
        <td>12</td>
        <td>299</td>
    </tr>
    <tr>
        <td>Different Perspective</td>
        <td>1</td>
        <td>2</td>
    </tr>
    <tr>
        <td>Different Perspective</td>
        <td>2</td>
        <td>3</td>
    </tr>
    <tr>
        <td>Different Perspective</td>
        <td>3</td>
        <td>4</td>
    </tr>
    <tr>
        <td>Different Perspective</td>
        <td>4</td>
        <td>8</td>
    </tr>
    <tr>
        <td>Different Perspective</td>
        <td>5</td>
        <td>12</td>
    </tr>
    <tr>
        <td>Different Perspective</td>
        <td>6</td>
        <td>11</td>
    </tr>
    <tr>
        <td>Different Perspective</td>
        <td>7</td>
        <td>8</td>
    </tr>
    <tr>
        <td>Different Perspective</td>
        <td>8</td>
        <td>10</td>
    </tr>
    <tr>
        <td>Different Perspective</td>
        <td>9</td>
        <td>12</td>
    </tr>
    <tr>
        <td>Different Perspective</td>
        <td>10</td>
        <td>4</td>
    </tr>
    <tr>
        <td>Different Perspective</td>
        <td>11</td>
        <td>6</td>
    </tr>
    <tr>
        <td>Different Perspective</td>
        <td>12</td>
        <td>9</td>
    </tr>
    <tr>
        <td>Expression Game</td>
        <td>1</td>
        <td>6</td>
    </tr>
    <tr>
        <td>Expression Game</td>
        <td>2</td>
        <td>9</td>
    </tr>
    <tr>
        <td>Expression Game</td>
        <td>3</td>
        <td>12</td>
    </tr>
    <tr>
        <td>Expression Game</td>
        <td>4</td>
        <td>10</td>
    </tr>
    <tr>
        <td>Expression Game</td>
        <td>5</td>
        <td>9</td>
    </tr>
    <tr>
        <td>Expression Game</td>
        <td>6</td>
        <td>11</td>
    </tr>
    <tr>
        <td>Expression Game</td>
        <td>7</td>
        <td>12</td>
    </tr>
    <tr>
        <td>Expression Game</td>
        <td>8</td>
        <td>11</td>
    </tr>
    <tr>
        <td>Expression Game</td>
        <td>9</td>
        <td>17</td>
    </tr>
    <tr>
        <td>Expression Game</td>
        <td>10</td>
        <td>3</td>
    </tr>
    <tr>
        <td>Expression Game</td>
        <td>11</td>
        <td>11</td>
    </tr>
    <tr>
        <td>Expression Game</td>
        <td>12</td>
        <td>13</td>
    </tr>
    <tr>
        <td>Eye Contact Game</td>
        <td>1</td>
        <td>624</td>
    </tr>
    <tr>
        <td>Eye Contact Game</td>
        <td>2</td>
        <td>564</td>
    </tr>
    <tr>
        <td>Eye Contact Game</td>
        <td>3</td>
        <td>589</td>
    </tr>
    <tr>
        <td>Eye Contact Game</td>
        <td>4</td>
        <td>449</td>
    </tr>
    <tr>
        <td>Eye Contact Game</td>
        <td>5</td>
        <td>1408</td>
    </tr>
    <tr>
        <td>Eye Contact Game</td>
        <td>6</td>
        <td>1812</td>
    </tr>
    <tr>
        <td>Eye Contact Game</td>
        <td>7</td>
        <td>1194</td>
    </tr>
    <tr>
        <td>Eye Contact Game</td>
        <td>8</td>
        <td>1130</td>
    </tr>
    <tr>
        <td>Eye Contact Game</td>
        <td>9</td>
        <td>1674</td>
    </tr>
    <tr>
        <td>Eye Contact Game</td>
        <td>10</td>
        <td>3452</td>
    </tr>
    <tr>
        <td>Eye Contact Game</td>
        <td>11</td>
        <td>889</td>
    </tr>
    <tr>
        <td>Eye Contact Game</td>
        <td>12</td>
        <td>760</td>
    </tr>
    <tr>
        <td>Eye Contact Warm-up</td>
        <td>1</td>
        <td>707</td>
    </tr>
    <tr>
        <td>Eye Contact Warm-up</td>
        <td>2</td>
        <td>616</td>
    </tr>
    <tr>
        <td>Eye Contact Warm-up</td>
        <td>3</td>
        <td>616</td>
    </tr>
    <tr>
        <td>Eye Contact Warm-up</td>
        <td>4</td>
        <td>454</td>
    </tr>
    <tr>
        <td>Eye Contact Warm-up</td>
        <td>5</td>
        <td>1636</td>
    </tr>
    <tr>
        <td>Eye Contact Warm-up</td>
        <td>6</td>
        <td>2152</td>
    </tr>
    <tr>
        <td>Eye Contact Warm-up</td>
        <td>7</td>
        <td>1379</td>
    </tr>
    <tr>
        <td>Eye Contact Warm-up</td>
        <td>8</td>
        <td>1256</td>
    </tr>
    <tr>
        <td>Eye Contact Warm-up</td>
        <td>9</td>
        <td>1967</td>
    </tr>
    <tr>
        <td>Eye Contact Warm-up</td>
        <td>10</td>
        <td>3675</td>
    </tr>
    <tr>
        <td>Eye Contact Warm-up</td>
        <td>11</td>
        <td>941</td>
    </tr>
    <tr>
        <td>Eye Contact Warm-up</td>
        <td>12</td>
        <td>839</td>
    </tr>
    <tr>
        <td>Foot Pointing</td>
        <td>1</td>
        <td>506</td>
    </tr>
    <tr>
        <td>Foot Pointing</td>
        <td>2</td>
        <td>433</td>
    </tr>
    <tr>
        <td>Foot Pointing</td>
        <td>3</td>
        <td>477</td>
    </tr>
    <tr>
        <td>Foot Pointing</td>
        <td>4</td>
        <td>339</td>
    </tr>
    <tr>
        <td>Foot Pointing</td>
        <td>5</td>
        <td>926</td>
    </tr>
    <tr>
        <td>Foot Pointing</td>
        <td>6</td>
        <td>1125</td>
    </tr>
    <tr>
        <td>Foot Pointing</td>
        <td>7</td>
        <td>759</td>
    </tr>
    <tr>
        <td>Foot Pointing</td>
        <td>8</td>
        <td>653</td>
    </tr>
    <tr>
        <td>Foot Pointing</td>
        <td>9</td>
        <td>992</td>
    </tr>
    <tr>
        <td>Foot Pointing</td>
        <td>10</td>
        <td>2290</td>
    </tr>
    <tr>
        <td>Foot Pointing</td>
        <td>11</td>
        <td>685</td>
    </tr>
    <tr>
        <td>Foot Pointing</td>
        <td>12</td>
        <td>566</td>
    </tr>
    <tr>
        <td>Impossible Task Game</td>
        <td>1</td>
        <td>49</td>
    </tr>
    <tr>
        <td>Impossible Task Game</td>
        <td>2</td>
        <td>48</td>
    </tr>
    <tr>
        <td>Impossible Task Game</td>
        <td>3</td>
        <td>36</td>
    </tr>
    <tr>
        <td>Impossible Task Game</td>
        <td>4</td>
        <td>43</td>
    </tr>
    <tr>
        <td>Impossible Task Game</td>
        <td>5</td>
        <td>49</td>
    </tr>
    <tr>
        <td>Impossible Task Game</td>
        <td>6</td>
        <td>59</td>
    </tr>
    <tr>
        <td>Impossible Task Game</td>
        <td>7</td>
        <td>50</td>
    </tr>
    <tr>
        <td>Impossible Task Game</td>
        <td>8</td>
        <td>32</td>
    </tr>
    <tr>
        <td>Impossible Task Game</td>
        <td>9</td>
        <td>35</td>
    </tr>
    <tr>
        <td>Impossible Task Game</td>
        <td>10</td>
        <td>37</td>
    </tr>
    <tr>
        <td>Impossible Task Game</td>
        <td>11</td>
        <td>48</td>
    </tr>
    <tr>
        <td>Impossible Task Game</td>
        <td>12</td>
        <td>46</td>
    </tr>
    <tr>
        <td>Impossible Task Warm-up</td>
        <td>1</td>
        <td>51</td>
    </tr>
    <tr>
        <td>Impossible Task Warm-up</td>
        <td>2</td>
        <td>49</td>
    </tr>
    <tr>
        <td>Impossible Task Warm-up</td>
        <td>3</td>
        <td>37</td>
    </tr>
    <tr>
        <td>Impossible Task Warm-up</td>
        <td>4</td>
        <td>43</td>
    </tr>
    <tr>
        <td>Impossible Task Warm-up</td>
        <td>5</td>
        <td>49</td>
    </tr>
    <tr>
        <td>Impossible Task Warm-up</td>
        <td>6</td>
        <td>58</td>
    </tr>
    <tr>
        <td>Impossible Task Warm-up</td>
        <td>7</td>
        <td>51</td>
    </tr>
    <tr>
        <td>Impossible Task Warm-up</td>
        <td>8</td>
        <td>34</td>
    </tr>
    <tr>
        <td>Impossible Task Warm-up</td>
        <td>9</td>
        <td>36</td>
    </tr>
    <tr>
        <td>Impossible Task Warm-up</td>
        <td>10</td>
        <td>36</td>
    </tr>
    <tr>
        <td>Impossible Task Warm-up</td>
        <td>11</td>
        <td>49</td>
    </tr>
    <tr>
        <td>Impossible Task Warm-up</td>
        <td>12</td>
        <td>46</td>
    </tr>
    <tr>
        <td>Inferential Reasoning Game</td>
        <td>1</td>
        <td>410</td>
    </tr>
    <tr>
        <td>Inferential Reasoning Game</td>
        <td>2</td>
        <td>297</td>
    </tr>
    <tr>
        <td>Inferential Reasoning Game</td>
        <td>3</td>
        <td>335</td>
    </tr>
    <tr>
        <td>Inferential Reasoning Game</td>
        <td>4</td>
        <td>254</td>
    </tr>
    <tr>
        <td>Inferential Reasoning Game</td>
        <td>5</td>
        <td>533</td>
    </tr>
    <tr>
        <td>Inferential Reasoning Game</td>
        <td>6</td>
        <td>544</td>
    </tr>
    <tr>
        <td>Inferential Reasoning Game</td>
        <td>7</td>
        <td>432</td>
    </tr>
    <tr>
        <td>Inferential Reasoning Game</td>
        <td>8</td>
        <td>350</td>
    </tr>
    <tr>
        <td>Inferential Reasoning Game</td>
        <td>9</td>
        <td>398</td>
    </tr>
    <tr>
        <td>Inferential Reasoning Game</td>
        <td>10</td>
        <td>785</td>
    </tr>
    <tr>
        <td>Inferential Reasoning Game</td>
        <td>11</td>
        <td>362</td>
    </tr>
    <tr>
        <td>Inferential Reasoning Game</td>
        <td>12</td>
        <td>280</td>
    </tr>
    <tr>
        <td>Inferential Reasoning Warm-up</td>
        <td>1</td>
        <td>425</td>
    </tr>
    <tr>
        <td>Inferential Reasoning Warm-up</td>
        <td>2</td>
        <td>302</td>
    </tr>
    <tr>
        <td>Inferential Reasoning Warm-up</td>
        <td>3</td>
        <td>351</td>
    </tr>
    <tr>
        <td>Inferential Reasoning Warm-up</td>
        <td>4</td>
        <td>257</td>
    </tr>
    <tr>
        <td>Inferential Reasoning Warm-up</td>
        <td>5</td>
        <td>544</td>
    </tr>
    <tr>
        <td>Inferential Reasoning Warm-up</td>
        <td>6</td>
        <td>550</td>
    </tr>
    <tr>
        <td>Inferential Reasoning Warm-up</td>
        <td>7</td>
        <td>450</td>
    </tr>
    <tr>
        <td>Inferential Reasoning Warm-up</td>
        <td>8</td>
        <td>354</td>
    </tr>
    <tr>
        <td>Inferential Reasoning Warm-up</td>
        <td>9</td>
        <td>399</td>
    </tr>
    <tr>
        <td>Inferential Reasoning Warm-up</td>
        <td>10</td>
        <td>794</td>
    </tr>
    <tr>
        <td>Inferential Reasoning Warm-up</td>
        <td>11</td>
        <td>376</td>
    </tr>
    <tr>
        <td>Inferential Reasoning Warm-up</td>
        <td>12</td>
        <td>296</td>
    </tr>
    <tr>
        <td>Memory versus Pointing</td>
        <td>1</td>
        <td>464</td>
    </tr>
    <tr>
        <td>Memory versus Pointing</td>
        <td>2</td>
        <td>395</td>
    </tr>
    <tr>
        <td>Memory versus Pointing</td>
        <td>3</td>
        <td>381</td>
    </tr>
    <tr>
        <td>Memory versus Pointing</td>
        <td>4</td>
        <td>299</td>
    </tr>
    <tr>
        <td>Memory versus Pointing</td>
        <td>5</td>
        <td>711</td>
    </tr>
    <tr>
        <td>Memory versus Pointing</td>
        <td>6</td>
        <td>704</td>
    </tr>
    <tr>
        <td>Memory versus Pointing</td>
        <td>7</td>
        <td>511</td>
    </tr>
    <tr>
        <td>Memory versus Pointing</td>
        <td>8</td>
        <td>415</td>
    </tr>
    <tr>
        <td>Memory versus Pointing</td>
        <td>9</td>
        <td>574</td>
    </tr>
    <tr>
        <td>Memory versus Pointing</td>
        <td>10</td>
        <td>1218</td>
    </tr>
    <tr>
        <td>Memory versus Pointing</td>
        <td>11</td>
        <td>477</td>
    </tr>
    <tr>
        <td>Memory versus Pointing</td>
        <td>12</td>
        <td>376</td>
    </tr>
    <tr>
        <td>Memory versus Smell</td>
        <td>1</td>
        <td>465</td>
    </tr>
    <tr>
        <td>Memory versus Smell</td>
        <td>2</td>
        <td>374</td>
    </tr>
    <tr>
        <td>Memory versus Smell</td>
        <td>3</td>
        <td>382</td>
    </tr>
    <tr>
        <td>Memory versus Smell</td>
        <td>4</td>
        <td>280</td>
    </tr>
    <tr>
        <td>Memory versus Smell</td>
        <td>5</td>
        <td>667</td>
    </tr>
    <tr>
        <td>Memory versus Smell</td>
        <td>6</td>
        <td>666</td>
    </tr>
    <tr>
        <td>Memory versus Smell</td>
        <td>7</td>
        <td>491</td>
    </tr>
    <tr>
        <td>Memory versus Smell</td>
        <td>8</td>
        <td>402</td>
    </tr>
    <tr>
        <td>Memory versus Smell</td>
        <td>9</td>
        <td>529</td>
    </tr>
    <tr>
        <td>Memory versus Smell</td>
        <td>10</td>
        <td>1111</td>
    </tr>
    <tr>
        <td>Memory versus Smell</td>
        <td>11</td>
        <td>444</td>
    </tr>
    <tr>
        <td>Memory versus Smell</td>
        <td>12</td>
        <td>352</td>
    </tr>
    <tr>
        <td>Navigation Game</td>
        <td>1</td>
        <td>57</td>
    </tr>
    <tr>
        <td>Navigation Game</td>
        <td>2</td>
        <td>41</td>
    </tr>
    <tr>
        <td>Navigation Game</td>
        <td>3</td>
        <td>47</td>
    </tr>
    <tr>
        <td>Navigation Game</td>
        <td>4</td>
        <td>41</td>
    </tr>
    <tr>
        <td>Navigation Game</td>
        <td>5</td>
        <td>336</td>
    </tr>
    <tr>
        <td>Navigation Game</td>
        <td>6</td>
        <td>81</td>
    </tr>
    <tr>
        <td>Navigation Game</td>
        <td>7</td>
        <td>70</td>
    </tr>
    <tr>
        <td>Navigation Game</td>
        <td>8</td>
        <td>41</td>
    </tr>
    <tr>
        <td>Navigation Game</td>
        <td>9</td>
        <td>52</td>
    </tr>
    <tr>
        <td>Navigation Game</td>
        <td>10</td>
        <td>69</td>
    </tr>
    <tr>
        <td>Navigation Game</td>
        <td>11</td>
        <td>47</td>
    </tr>
    <tr>
        <td>Navigation Game</td>
        <td>12</td>
        <td>45</td>
    </tr>
    <tr>
        <td>Navigation Learning</td>
        <td>1</td>
        <td>59</td>
    </tr>
    <tr>
        <td>Navigation Learning</td>
        <td>2</td>
        <td>43</td>
    </tr>
    <tr>
        <td>Navigation Learning</td>
        <td>3</td>
        <td>47</td>
    </tr>
    <tr>
        <td>Navigation Learning</td>
        <td>4</td>
        <td>45</td>
    </tr>
    <tr>
        <td>Navigation Learning</td>
        <td>5</td>
        <td>444</td>
    </tr>
    <tr>
        <td>Navigation Learning</td>
        <td>6</td>
        <td>90</td>
    </tr>
    <tr>
        <td>Navigation Learning</td>
        <td>7</td>
        <td>74</td>
    </tr>
    <tr>
        <td>Navigation Learning</td>
        <td>8</td>
        <td>34</td>
    </tr>
    <tr>
        <td>Navigation Learning</td>
        <td>9</td>
        <td>54</td>
    </tr>
    <tr>
        <td>Navigation Learning</td>
        <td>10</td>
        <td>70</td>
    </tr>
    <tr>
        <td>Navigation Learning</td>
        <td>11</td>
        <td>47</td>
    </tr>
    <tr>
        <td>Navigation Learning</td>
        <td>12</td>
        <td>47</td>
    </tr>
    <tr>
        <td>Navigation Warm-up</td>
        <td>1</td>
        <td>62</td>
    </tr>
    <tr>
        <td>Navigation Warm-up</td>
        <td>2</td>
        <td>43</td>
    </tr>
    <tr>
        <td>Navigation Warm-up</td>
        <td>3</td>
        <td>50</td>
    </tr>
    <tr>
        <td>Navigation Warm-up</td>
        <td>4</td>
        <td>42</td>
    </tr>
    <tr>
        <td>Navigation Warm-up</td>
        <td>5</td>
        <td>625</td>
    </tr>
    <tr>
        <td>Navigation Warm-up</td>
        <td>6</td>
        <td>114</td>
    </tr>
    <tr>
        <td>Navigation Warm-up</td>
        <td>7</td>
        <td>88</td>
    </tr>
    <tr>
        <td>Navigation Warm-up</td>
        <td>8</td>
        <td>40</td>
    </tr>
    <tr>
        <td>Navigation Warm-up</td>
        <td>9</td>
        <td>58</td>
    </tr>
    <tr>
        <td>Navigation Warm-up</td>
        <td>10</td>
        <td>76</td>
    </tr>
    <tr>
        <td>Navigation Warm-up</td>
        <td>11</td>
        <td>52</td>
    </tr>
    <tr>
        <td>Navigation Warm-up</td>
        <td>12</td>
        <td>49</td>
    </tr>
    <tr>
        <td>Numerosity Warm-Up</td>
        <td>1</td>
        <td>36</td>
    </tr>
    <tr>
        <td>Numerosity Warm-Up</td>
        <td>2</td>
        <td>28</td>
    </tr>
    <tr>
        <td>Numerosity Warm-Up</td>
        <td>3</td>
        <td>35</td>
    </tr>
    <tr>
        <td>Numerosity Warm-Up</td>
        <td>4</td>
        <td>17</td>
    </tr>
    <tr>
        <td>Numerosity Warm-Up</td>
        <td>5</td>
        <td>37</td>
    </tr>
    <tr>
        <td>Numerosity Warm-Up</td>
        <td>6</td>
        <td>44</td>
    </tr>
    <tr>
        <td>Numerosity Warm-Up</td>
        <td>7</td>
        <td>37</td>
    </tr>
    <tr>
        <td>Numerosity Warm-Up</td>
        <td>8</td>
        <td>23</td>
    </tr>
    <tr>
        <td>Numerosity Warm-Up</td>
        <td>9</td>
        <td>24</td>
    </tr>
    <tr>
        <td>Numerosity Warm-Up</td>
        <td>10</td>
        <td>29</td>
    </tr>
    <tr>
        <td>Numerosity Warm-Up</td>
        <td>11</td>
        <td>26</td>
    </tr>
    <tr>
        <td>Numerosity Warm-Up</td>
        <td>12</td>
        <td>46</td>
    </tr>
    <tr>
        <td>One Cup Warm-up</td>
        <td>1</td>
        <td>476</td>
    </tr>
    <tr>
        <td>One Cup Warm-up</td>
        <td>2</td>
        <td>388</td>
    </tr>
    <tr>
        <td>One Cup Warm-up</td>
        <td>3</td>
        <td>388</td>
    </tr>
    <tr>
        <td>One Cup Warm-up</td>
        <td>4</td>
        <td>313</td>
    </tr>
    <tr>
        <td>One Cup Warm-up</td>
        <td>5</td>
        <td>757</td>
    </tr>
    <tr>
        <td>One Cup Warm-up</td>
        <td>6</td>
        <td>745</td>
    </tr>
    <tr>
        <td>One Cup Warm-up</td>
        <td>7</td>
        <td>536</td>
    </tr>
    <tr>
        <td>One Cup Warm-up</td>
        <td>8</td>
        <td>416</td>
    </tr>
    <tr>
        <td>One Cup Warm-up</td>
        <td>9</td>
        <td>602</td>
    </tr>
    <tr>
        <td>One Cup Warm-up</td>
        <td>10</td>
        <td>1272</td>
    </tr>
    <tr>
        <td>One Cup Warm-up</td>
        <td>11</td>
        <td>491</td>
    </tr>
    <tr>
        <td>One Cup Warm-up</td>
        <td>12</td>
        <td>401</td>
    </tr>
    <tr>
        <td>Physical Reasoning Game</td>
        <td>1</td>
        <td>317</td>
    </tr>
    <tr>
        <td>Physical Reasoning Game</td>
        <td>2</td>
        <td>252</td>
    </tr>
    <tr>
        <td>Physical Reasoning Game</td>
        <td>3</td>
        <td>321</td>
    </tr>
    <tr>
        <td>Physical Reasoning Game</td>
        <td>4</td>
        <td>224</td>
    </tr>
    <tr>
        <td>Physical Reasoning Game</td>
        <td>5</td>
        <td>430</td>
    </tr>
    <tr>
        <td>Physical Reasoning Game</td>
        <td>6</td>
        <td>424</td>
    </tr>
    <tr>
        <td>Physical Reasoning Game</td>
        <td>7</td>
        <td>360</td>
    </tr>
    <tr>
        <td>Physical Reasoning Game</td>
        <td>8</td>
        <td>316</td>
    </tr>
    <tr>
        <td>Physical Reasoning Game</td>
        <td>9</td>
        <td>309</td>
    </tr>
    <tr>
        <td>Physical Reasoning Game</td>
        <td>10</td>
        <td>711</td>
    </tr>
    <tr>
        <td>Physical Reasoning Game</td>
        <td>11</td>
        <td>341</td>
    </tr>
    <tr>
        <td>Physical Reasoning Game</td>
        <td>12</td>
        <td>250</td>
    </tr>
    <tr>
        <td>Physical Reasoning Warm-up</td>
        <td>1</td>
        <td>384</td>
    </tr>
    <tr>
        <td>Physical Reasoning Warm-up</td>
        <td>2</td>
        <td>290</td>
    </tr>
    <tr>
        <td>Physical Reasoning Warm-up</td>
        <td>3</td>
        <td>337</td>
    </tr>
    <tr>
        <td>Physical Reasoning Warm-up</td>
        <td>4</td>
        <td>247</td>
    </tr>
    <tr>
        <td>Physical Reasoning Warm-up</td>
        <td>5</td>
        <td>510</td>
    </tr>
    <tr>
        <td>Physical Reasoning Warm-up</td>
        <td>6</td>
        <td>504</td>
    </tr>
    <tr>
        <td>Physical Reasoning Warm-up</td>
        <td>7</td>
        <td>411</td>
    </tr>
    <tr>
        <td>Physical Reasoning Warm-up</td>
        <td>8</td>
        <td>347</td>
    </tr>
    <tr>
        <td>Physical Reasoning Warm-up</td>
        <td>9</td>
        <td>364</td>
    </tr>
    <tr>
        <td>Physical Reasoning Warm-up</td>
        <td>10</td>
        <td>742</td>
    </tr>
    <tr>
        <td>Physical Reasoning Warm-up</td>
        <td>11</td>
        <td>349</td>
    </tr>
    <tr>
        <td>Physical Reasoning Warm-up</td>
        <td>12</td>
        <td>276</td>
    </tr>
    <tr>
        <td>Self Control Game</td>
        <td>1</td>
        <td>8</td>
    </tr>
    <tr>
        <td>Self Control Game</td>
        <td>2</td>
        <td>8</td>
    </tr>
    <tr>
        <td>Self Control Game</td>
        <td>3</td>
        <td>11</td>
    </tr>
    <tr>
        <td>Self Control Game</td>
        <td>4</td>
        <td>9</td>
    </tr>
    <tr>
        <td>Self Control Game</td>
        <td>5</td>
        <td>9</td>
    </tr>
    <tr>
        <td>Self Control Game</td>
        <td>6</td>
        <td>11</td>
    </tr>
    <tr>
        <td>Self Control Game</td>
        <td>7</td>
        <td>14</td>
    </tr>
    <tr>
        <td>Self Control Game</td>
        <td>8</td>
        <td>13</td>
    </tr>
    <tr>
        <td>Self Control Game</td>
        <td>9</td>
        <td>19</td>
    </tr>
    <tr>
        <td>Self Control Game</td>
        <td>10</td>
        <td>9</td>
    </tr>
    <tr>
        <td>Self Control Game</td>
        <td>11</td>
        <td>15</td>
    </tr>
    <tr>
        <td>Self Control Game</td>
        <td>12</td>
        <td>6</td>
    </tr>
    <tr>
        <td>Shaker Game</td>
        <td>1</td>
        <td>2</td>
    </tr>
    <tr>
        <td>Shaker Game</td>
        <td>2</td>
        <td>9</td>
    </tr>
    <tr>
        <td>Shaker Game</td>
        <td>3</td>
        <td>8</td>
    </tr>
    <tr>
        <td>Shaker Game</td>
        <td>4</td>
        <td>4</td>
    </tr>
    <tr>
        <td>Shaker Game</td>
        <td>5</td>
        <td>10</td>
    </tr>
    <tr>
        <td>Shaker Game</td>
        <td>6</td>
        <td>7</td>
    </tr>
    <tr>
        <td>Shaker Game</td>
        <td>7</td>
        <td>5</td>
    </tr>
    <tr>
        <td>Shaker Game</td>
        <td>8</td>
        <td>6</td>
    </tr>
    <tr>
        <td>Shaker Game</td>
        <td>9</td>
        <td>12</td>
    </tr>
    <tr>
        <td>Shaker Game</td>
        <td>10</td>
        <td>10</td>
    </tr>
    <tr>
        <td>Shaker Game</td>
        <td>11</td>
        <td>3</td>
    </tr>
    <tr>
        <td>Shaker Game</td>
        <td>12</td>
        <td>1</td>
    </tr>
    <tr>
        <td>Shaker Warm-Up</td>
        <td>1</td>
        <td>2</td>
    </tr>
    <tr>
        <td>Shaker Warm-Up</td>
        <td>2</td>
        <td>11</td>
    </tr>
    <tr>
        <td>Shaker Warm-Up</td>
        <td>3</td>
        <td>8</td>
    </tr>
    <tr>
        <td>Shaker Warm-Up</td>
        <td>4</td>
        <td>4</td>
    </tr>
    <tr>
        <td>Shaker Warm-Up</td>
        <td>5</td>
        <td>10</td>
    </tr>
    <tr>
        <td>Shaker Warm-Up</td>
        <td>6</td>
        <td>7</td>
    </tr>
    <tr>
        <td>Shaker Warm-Up</td>
        <td>7</td>
        <td>5</td>
    </tr>
    <tr>
        <td>Shaker Warm-Up</td>
        <td>8</td>
        <td>6</td>
    </tr>
    <tr>
        <td>Shaker Warm-Up</td>
        <td>9</td>
        <td>13</td>
    </tr>
    <tr>
        <td>Shaker Warm-Up</td>
        <td>10</td>
        <td>11</td>
    </tr>
    <tr>
        <td>Shaker Warm-Up</td>
        <td>11</td>
        <td>3</td>
    </tr>
    <tr>
        <td>Shaker Warm-Up</td>
        <td>12</td>
        <td>1</td>
    </tr>
    <tr>
        <td>Shared Perspective</td>
        <td>1</td>
        <td>1</td>
    </tr>
    <tr>
        <td>Shared Perspective</td>
        <td>2</td>
        <td>3</td>
    </tr>
    <tr>
        <td>Shared Perspective</td>
        <td>3</td>
        <td>3</td>
    </tr>
    <tr>
        <td>Shared Perspective</td>
        <td>4</td>
        <td>8</td>
    </tr>
    <tr>
        <td>Shared Perspective</td>
        <td>5</td>
        <td>11</td>
    </tr>
    <tr>
        <td>Shared Perspective</td>
        <td>6</td>
        <td>11</td>
    </tr>
    <tr>
        <td>Shared Perspective</td>
        <td>7</td>
        <td>7</td>
    </tr>
    <tr>
        <td>Shared Perspective</td>
        <td>8</td>
        <td>10</td>
    </tr>
    <tr>
        <td>Shared Perspective</td>
        <td>9</td>
        <td>12</td>
    </tr>
    <tr>
        <td>Shared Perspective</td>
        <td>10</td>
        <td>4</td>
    </tr>
    <tr>
        <td>Shared Perspective</td>
        <td>11</td>
        <td>6</td>
    </tr>
    <tr>
        <td>Shared Perspective</td>
        <td>12</td>
        <td>7</td>
    </tr>
    <tr>
        <td>Slide</td>
        <td>1</td>
        <td>17</td>
    </tr>
    <tr>
        <td>Slide</td>
        <td>2</td>
        <td>12</td>
    </tr>
    <tr>
        <td>Slide</td>
        <td>3</td>
        <td>16</td>
    </tr>
    <tr>
        <td>Slide</td>
        <td>4</td>
        <td>11</td>
    </tr>
    <tr>
        <td>Slide</td>
        <td>5</td>
        <td>17</td>
    </tr>
    <tr>
        <td>Slide</td>
        <td>6</td>
        <td>10</td>
    </tr>
    <tr>
        <td>Slide</td>
        <td>7</td>
        <td>13</td>
    </tr>
    <tr>
        <td>Slide</td>
        <td>8</td>
        <td>6</td>
    </tr>
    <tr>
        <td>Slide</td>
        <td>9</td>
        <td>18</td>
    </tr>
    <tr>
        <td>Slide</td>
        <td>10</td>
        <td>7</td>
    </tr>
    <tr>
        <td>Slide</td>
        <td>11</td>
        <td>13</td>
    </tr>
    <tr>
        <td>Slide</td>
        <td>12</td>
        <td>7</td>
    </tr>
    <tr>
        <td>Smell Game</td>
        <td>1</td>
        <td>13</td>
    </tr>
    <tr>
        <td>Smell Game</td>
        <td>2</td>
        <td>18</td>
    </tr>
    <tr>
        <td>Smell Game</td>
        <td>3</td>
        <td>16</td>
    </tr>
    <tr>
        <td>Smell Game</td>
        <td>4</td>
        <td>6</td>
    </tr>
    <tr>
        <td>Smell Game</td>
        <td>5</td>
        <td>19</td>
    </tr>
    <tr>
        <td>Smell Game</td>
        <td>6</td>
        <td>9</td>
    </tr>
    <tr>
        <td>Smell Game</td>
        <td>7</td>
        <td>21</td>
    </tr>
    <tr>
        <td>Smell Game</td>
        <td>8</td>
        <td>10</td>
    </tr>
    <tr>
        <td>Smell Game</td>
        <td>9</td>
        <td>16</td>
    </tr>
    <tr>
        <td>Smell Game</td>
        <td>10</td>
        <td>15</td>
    </tr>
    <tr>
        <td>Smell Game</td>
        <td>11</td>
        <td>12</td>
    </tr>
    <tr>
        <td>Smell Game</td>
        <td>12</td>
        <td>13</td>
    </tr>
    <tr>
        <td>Stair Game</td>
        <td>1</td>
        <td>12</td>
    </tr>
    <tr>
        <td>Stair Game</td>
        <td>2</td>
        <td>8</td>
    </tr>
    <tr>
        <td>Stair Game</td>
        <td>3</td>
        <td>7</td>
    </tr>
    <tr>
        <td>Stair Game</td>
        <td>4</td>
        <td>4</td>
    </tr>
    <tr>
        <td>Stair Game</td>
        <td>5</td>
        <td>10</td>
    </tr>
    <tr>
        <td>Stair Game</td>
        <td>6</td>
        <td>7</td>
    </tr>
    <tr>
        <td>Stair Game</td>
        <td>7</td>
        <td>14</td>
    </tr>
    <tr>
        <td>Stair Game</td>
        <td>8</td>
        <td>15</td>
    </tr>
    <tr>
        <td>Stair Game</td>
        <td>9</td>
        <td>17</td>
    </tr>
    <tr>
        <td>Stair Game</td>
        <td>10</td>
        <td>7</td>
    </tr>
    <tr>
        <td>Stair Game</td>
        <td>11</td>
        <td>3</td>
    </tr>
    <tr>
        <td>Stair Game</td>
        <td>12</td>
        <td>8</td>
    </tr>
    <tr>
        <td>Switch</td>
        <td>1</td>
        <td>15</td>
    </tr>
    <tr>
        <td>Switch</td>
        <td>2</td>
        <td>12</td>
    </tr>
    <tr>
        <td>Switch</td>
        <td>3</td>
        <td>14</td>
    </tr>
    <tr>
        <td>Switch</td>
        <td>4</td>
        <td>11</td>
    </tr>
    <tr>
        <td>Switch</td>
        <td>5</td>
        <td>15</td>
    </tr>
    <tr>
        <td>Switch</td>
        <td>6</td>
        <td>11</td>
    </tr>
    <tr>
        <td>Switch</td>
        <td>7</td>
        <td>11</td>
    </tr>
    <tr>
        <td>Switch</td>
        <td>8</td>
        <td>10</td>
    </tr>
    <tr>
        <td>Switch</td>
        <td>9</td>
        <td>13</td>
    </tr>
    <tr>
        <td>Switch</td>
        <td>10</td>
        <td>9</td>
    </tr>
    <tr>
        <td>Switch</td>
        <td>11</td>
        <td>10</td>
    </tr>
    <tr>
        <td>Switch</td>
        <td>12</td>
        <td>6</td>
    </tr>
    <tr>
        <td>Treat Warm-up</td>
        <td>1</td>
        <td>626</td>
    </tr>
    <tr>
        <td>Treat Warm-up</td>
        <td>2</td>
        <td>495</td>
    </tr>
    <tr>
        <td>Treat Warm-up</td>
        <td>3</td>
        <td>515</td>
    </tr>
    <tr>
        <td>Treat Warm-up</td>
        <td>4</td>
        <td>393</td>
    </tr>
    <tr>
        <td>Treat Warm-up</td>
        <td>5</td>
        <td>1182</td>
    </tr>
    <tr>
        <td>Treat Warm-up</td>
        <td>6</td>
        <td>1444</td>
    </tr>
    <tr>
        <td>Treat Warm-up</td>
        <td>7</td>
        <td>951</td>
    </tr>
    <tr>
        <td>Treat Warm-up</td>
        <td>8</td>
        <td>791</td>
    </tr>
    <tr>
        <td>Treat Warm-up</td>
        <td>9</td>
        <td>1303</td>
    </tr>
    <tr>
        <td>Treat Warm-up</td>
        <td>10</td>
        <td>2626</td>
    </tr>
    <tr>
        <td>Treat Warm-up</td>
        <td>11</td>
        <td>744</td>
    </tr>
    <tr>
        <td>Treat Warm-up</td>
        <td>12</td>
        <td>667</td>
    </tr>
    <tr>
        <td>Turn Your Back</td>
        <td>1</td>
        <td>462</td>
    </tr>
    <tr>
        <td>Turn Your Back</td>
        <td>2</td>
        <td>372</td>
    </tr>
    <tr>
        <td>Turn Your Back</td>
        <td>3</td>
        <td>418</td>
    </tr>
    <tr>
        <td>Turn Your Back</td>
        <td>4</td>
        <td>298</td>
    </tr>
    <tr>
        <td>Turn Your Back</td>
        <td>5</td>
        <td>769</td>
    </tr>
    <tr>
        <td>Turn Your Back</td>
        <td>6</td>
        <td>778</td>
    </tr>
    <tr>
        <td>Turn Your Back</td>
        <td>7</td>
        <td>535</td>
    </tr>
    <tr>
        <td>Turn Your Back</td>
        <td>8</td>
        <td>418</td>
    </tr>
    <tr>
        <td>Turn Your Back</td>
        <td>9</td>
        <td>599</td>
    </tr>
    <tr>
        <td>Turn Your Back</td>
        <td>10</td>
        <td>1711</td>
    </tr>
    <tr>
        <td>Turn Your Back</td>
        <td>11</td>
        <td>601</td>
    </tr>
    <tr>
        <td>Turn Your Back</td>
        <td>12</td>
        <td>467</td>
    </tr>
    <tr>
        <td>Two Cup Warm-up</td>
        <td>1</td>
        <td>490</td>
    </tr>
    <tr>
        <td>Two Cup Warm-up</td>
        <td>2</td>
        <td>386</td>
    </tr>
    <tr>
        <td>Two Cup Warm-up</td>
        <td>3</td>
        <td>389</td>
    </tr>
    <tr>
        <td>Two Cup Warm-up</td>
        <td>4</td>
        <td>308</td>
    </tr>
    <tr>
        <td>Two Cup Warm-up</td>
        <td>5</td>
        <td>747</td>
    </tr>
    <tr>
        <td>Two Cup Warm-up</td>
        <td>6</td>
        <td>732</td>
    </tr>
    <tr>
        <td>Two Cup Warm-up</td>
        <td>7</td>
        <td>537</td>
    </tr>
    <tr>
        <td>Two Cup Warm-up</td>
        <td>8</td>
        <td>419</td>
    </tr>
    <tr>
        <td>Two Cup Warm-up</td>
        <td>9</td>
        <td>578</td>
    </tr>
    <tr>
        <td>Two Cup Warm-up</td>
        <td>10</td>
        <td>1234</td>
    </tr>
    <tr>
        <td>Two Cup Warm-up</td>
        <td>11</td>
        <td>482</td>
    </tr>
    <tr>
        <td>Two Cup Warm-up</td>
        <td>12</td>
        <td>379</td>
    </tr>
    <tr>
        <td>Warm-up</td>
        <td>1</td>
        <td>70</td>
    </tr>
    <tr>
        <td>Warm-up</td>
        <td>2</td>
        <td>77</td>
    </tr>
    <tr>
        <td>Warm-Up</td>
        <td>3</td>
        <td>79</td>
    </tr>
    <tr>
        <td>Warm-Up</td>
        <td>4</td>
        <td>54</td>
    </tr>
    <tr>
        <td>Warm-Up</td>
        <td>5</td>
        <td>71</td>
    </tr>
    <tr>
        <td>Warm-Up</td>
        <td>6</td>
        <td>64</td>
    </tr>
    <tr>
        <td>Warm-Up</td>
        <td>7</td>
        <td>101</td>
    </tr>
    <tr>
        <td>Warm-Up</td>
        <td>8</td>
        <td>64</td>
    </tr>
    <tr>
        <td>Warm-Up</td>
        <td>9</td>
        <td>103</td>
    </tr>
    <tr>
        <td>Warm-up</td>
        <td>10</td>
        <td>69</td>
    </tr>
    <tr>
        <td>Warm-Up</td>
        <td>11</td>
        <td>65</td>
    </tr>
    <tr>
        <td>Warm-up</td>
        <td>12</td>
        <td>56</td>
    </tr>
    <tr>
        <td>Watching</td>
        <td>1</td>
        <td>594</td>
    </tr>
    <tr>
        <td>Watching</td>
        <td>2</td>
        <td>443</td>
    </tr>
    <tr>
        <td>Watching</td>
        <td>3</td>
        <td>472</td>
    </tr>
    <tr>
        <td>Watching</td>
        <td>4</td>
        <td>322</td>
    </tr>
    <tr>
        <td>Watching</td>
        <td>5</td>
        <td>980</td>
    </tr>
    <tr>
        <td>Watching</td>
        <td>6</td>
        <td>1035</td>
    </tr>
    <tr>
        <td>Watching</td>
        <td>7</td>
        <td>679</td>
    </tr>
    <tr>
        <td>Watching</td>
        <td>8</td>
        <td>511</td>
    </tr>
    <tr>
        <td>Watching</td>
        <td>9</td>
        <td>809</td>
    </tr>
    <tr>
        <td>Watching</td>
        <td>10</td>
        <td>1797</td>
    </tr>
    <tr>
        <td>Watching</td>
        <td>11</td>
        <td>611</td>
    </tr>
    <tr>
        <td>Watching</td>
        <td>12</td>
        <td>555</td>
    </tr>
    <tr>
        <td>Watching - Part 2</td>
        <td>1</td>
        <td>445</td>
    </tr>
    <tr>
        <td>Watching - Part 2</td>
        <td>2</td>
        <td>372</td>
    </tr>
    <tr>
        <td>Watching - Part 2</td>
        <td>3</td>
        <td>406</td>
    </tr>
    <tr>
        <td>Watching - Part 2</td>
        <td>4</td>
        <td>282</td>
    </tr>
    <tr>
        <td>Watching - Part 2</td>
        <td>5</td>
        <td>734</td>
    </tr>
    <tr>
        <td>Watching - Part 2</td>
        <td>6</td>
        <td>747</td>
    </tr>
    <tr>
        <td>Watching - Part 2</td>
        <td>7</td>
        <td>504</td>
    </tr>
    <tr>
        <td>Watching - Part 2</td>
        <td>8</td>
        <td>405</td>
    </tr>
    <tr>
        <td>Watching - Part 2</td>
        <td>9</td>
        <td>568</td>
    </tr>
    <tr>
        <td>Watching - Part 2</td>
        <td>10</td>
        <td>1578</td>
    </tr>
    <tr>
        <td>Watching - Part 2</td>
        <td>11</td>
        <td>565</td>
    </tr>
    <tr>
        <td>Watching - Part 2</td>
        <td>12</td>
        <td>438</td>
    </tr>
    <tr>
        <td>Yawn Game</td>
        <td>1</td>
        <td>828</td>
    </tr>
    <tr>
        <td>Yawn Game</td>
        <td>2</td>
        <td>709</td>
    </tr>
    <tr>
        <td>Yawn Game</td>
        <td>3</td>
        <td>681</td>
    </tr>
    <tr>
        <td>Yawn Game</td>
        <td>4</td>
        <td>525</td>
    </tr>
    <tr>
        <td>Yawn Game</td>
        <td>5</td>
        <td>2065</td>
    </tr>
    <tr>
        <td>Yawn Game</td>
        <td>6</td>
        <td>2906</td>
    </tr>
    <tr>
        <td>Yawn Game</td>
        <td>7</td>
        <td>1775</td>
    </tr>
    <tr>
        <td>Yawn Game</td>
        <td>8</td>
        <td>1520</td>
    </tr>
    <tr>
        <td>Yawn Game</td>
        <td>9</td>
        <td>2563</td>
    </tr>
    <tr>
        <td>Yawn Game</td>
        <td>10</td>
        <td>4073</td>
    </tr>
    <tr>
        <td>Yawn Game</td>
        <td>11</td>
        <td>989</td>
    </tr>
    <tr>
        <td>Yawn Game</td>
        <td>12</td>
        <td>978</td>
    </tr>
    <tr>
        <td>Yawn Warm-up</td>
        <td>1</td>
        <td>834</td>
    </tr>
    <tr>
        <td>Yawn Warm-up</td>
        <td>2</td>
        <td>712</td>
    </tr>
    <tr>
        <td>Yawn Warm-up</td>
        <td>3</td>
        <td>698</td>
    </tr>
    <tr>
        <td>Yawn Warm-up</td>
        <td>4</td>
        <td>541</td>
    </tr>
    <tr>
        <td>Yawn Warm-up</td>
        <td>5</td>
        <td>2143</td>
    </tr>
    <tr>
        <td>Yawn Warm-up</td>
        <td>6</td>
        <td>3071</td>
    </tr>
    <tr>
        <td>Yawn Warm-up</td>
        <td>7</td>
        <td>1909</td>
    </tr>
    <tr>
        <td>Yawn Warm-up</td>
        <td>8</td>
        <td>1694</td>
    </tr>
    <tr>
        <td>Yawn Warm-up</td>
        <td>9</td>
        <td>2771</td>
    </tr>
    <tr>
        <td>Yawn Warm-up</td>
        <td>10</td>
        <td>4387</td>
    </tr>
    <tr>
        <td>Yawn Warm-up</td>
        <td>11</td>
        <td>1060</td>
    </tr>
    <tr>
        <td>Yawn Warm-up</td>
        <td>12</td>
        <td>1043</td>
    </tr>
</table>




```python
%%sql
SELECT test_name, MONTh(created_at) AS Month, COUNT(created_at) AS Num_Completed_Tests
FROM complete_tests
GROUP BY MONTH, test_name;
```

    480 rows affected.





<table>
    <tr>
        <th>test_name</th>
        <th>Month</th>
        <th>Num_Completed_Tests</th>
    </tr>
    <tr>
        <td>1 vs 1 Game</td>
        <td>1</td>
        <td>25</td>
    </tr>
    <tr>
        <td>3 vs 1 Game</td>
        <td>1</td>
        <td>35</td>
    </tr>
    <tr>
        <td>5 vs 1 Game</td>
        <td>1</td>
        <td>59</td>
    </tr>
    <tr>
        <td>Arm Pointing</td>
        <td>1</td>
        <td>622</td>
    </tr>
    <tr>
        <td>Cover Your Eyes</td>
        <td>1</td>
        <td>452</td>
    </tr>
    <tr>
        <td>Delayed Cup Game</td>
        <td>1</td>
        <td>356</td>
    </tr>
    <tr>
        <td>Different Perspective</td>
        <td>1</td>
        <td>2</td>
    </tr>
    <tr>
        <td>Expression Game</td>
        <td>1</td>
        <td>6</td>
    </tr>
    <tr>
        <td>Eye Contact Game</td>
        <td>1</td>
        <td>624</td>
    </tr>
    <tr>
        <td>Eye Contact Warm-up</td>
        <td>1</td>
        <td>707</td>
    </tr>
    <tr>
        <td>Foot Pointing</td>
        <td>1</td>
        <td>506</td>
    </tr>
    <tr>
        <td>Impossible Task Game</td>
        <td>1</td>
        <td>49</td>
    </tr>
    <tr>
        <td>Impossible Task Warm-up</td>
        <td>1</td>
        <td>51</td>
    </tr>
    <tr>
        <td>Inferential Reasoning Game</td>
        <td>1</td>
        <td>410</td>
    </tr>
    <tr>
        <td>Inferential Reasoning Warm-up</td>
        <td>1</td>
        <td>425</td>
    </tr>
    <tr>
        <td>Memory versus Pointing</td>
        <td>1</td>
        <td>464</td>
    </tr>
    <tr>
        <td>Memory versus Smell</td>
        <td>1</td>
        <td>465</td>
    </tr>
    <tr>
        <td>Navigation Game</td>
        <td>1</td>
        <td>57</td>
    </tr>
    <tr>
        <td>Navigation Learning</td>
        <td>1</td>
        <td>59</td>
    </tr>
    <tr>
        <td>Navigation Warm-up</td>
        <td>1</td>
        <td>62</td>
    </tr>
    <tr>
        <td>Numerosity Warm-Up</td>
        <td>1</td>
        <td>36</td>
    </tr>
    <tr>
        <td>One Cup Warm-up</td>
        <td>1</td>
        <td>476</td>
    </tr>
    <tr>
        <td>Physical Reasoning Game</td>
        <td>1</td>
        <td>317</td>
    </tr>
    <tr>
        <td>Physical Reasoning Warm-up</td>
        <td>1</td>
        <td>384</td>
    </tr>
    <tr>
        <td>Self Control Game</td>
        <td>1</td>
        <td>8</td>
    </tr>
    <tr>
        <td>Shaker Game</td>
        <td>1</td>
        <td>2</td>
    </tr>
    <tr>
        <td>Shaker Warm-Up</td>
        <td>1</td>
        <td>2</td>
    </tr>
    <tr>
        <td>Shared Perspective</td>
        <td>1</td>
        <td>1</td>
    </tr>
    <tr>
        <td>Slide</td>
        <td>1</td>
        <td>17</td>
    </tr>
    <tr>
        <td>Smell Game</td>
        <td>1</td>
        <td>13</td>
    </tr>
    <tr>
        <td>Stair Game</td>
        <td>1</td>
        <td>12</td>
    </tr>
    <tr>
        <td>Switch</td>
        <td>1</td>
        <td>15</td>
    </tr>
    <tr>
        <td>Treat Warm-up</td>
        <td>1</td>
        <td>626</td>
    </tr>
    <tr>
        <td>Turn Your Back</td>
        <td>1</td>
        <td>462</td>
    </tr>
    <tr>
        <td>Two Cup Warm-up</td>
        <td>1</td>
        <td>490</td>
    </tr>
    <tr>
        <td>Warm-up</td>
        <td>1</td>
        <td>70</td>
    </tr>
    <tr>
        <td>Watching</td>
        <td>1</td>
        <td>594</td>
    </tr>
    <tr>
        <td>Watching - Part 2</td>
        <td>1</td>
        <td>445</td>
    </tr>
    <tr>
        <td>Yawn Game</td>
        <td>1</td>
        <td>828</td>
    </tr>
    <tr>
        <td>Yawn Warm-up</td>
        <td>1</td>
        <td>834</td>
    </tr>
    <tr>
        <td>1 vs 1 Game</td>
        <td>2</td>
        <td>28</td>
    </tr>
    <tr>
        <td>3 vs 1 Game</td>
        <td>2</td>
        <td>28</td>
    </tr>
    <tr>
        <td>5 vs 1 Game</td>
        <td>2</td>
        <td>54</td>
    </tr>
    <tr>
        <td>Arm Pointing</td>
        <td>2</td>
        <td>498</td>
    </tr>
    <tr>
        <td>Cover Your Eyes</td>
        <td>2</td>
        <td>373</td>
    </tr>
    <tr>
        <td>Delayed Cup Game</td>
        <td>2</td>
        <td>319</td>
    </tr>
    <tr>
        <td>Different Perspective</td>
        <td>2</td>
        <td>3</td>
    </tr>
    <tr>
        <td>Expression Game</td>
        <td>2</td>
        <td>9</td>
    </tr>
    <tr>
        <td>Eye Contact Game</td>
        <td>2</td>
        <td>564</td>
    </tr>
    <tr>
        <td>Eye Contact Warm-up</td>
        <td>2</td>
        <td>616</td>
    </tr>
    <tr>
        <td>Foot Pointing</td>
        <td>2</td>
        <td>433</td>
    </tr>
    <tr>
        <td>Impossible Task Game</td>
        <td>2</td>
        <td>48</td>
    </tr>
    <tr>
        <td>Impossible Task Warm-up</td>
        <td>2</td>
        <td>49</td>
    </tr>
    <tr>
        <td>Inferential Reasoning Game</td>
        <td>2</td>
        <td>297</td>
    </tr>
    <tr>
        <td>Inferential Reasoning Warm-up</td>
        <td>2</td>
        <td>302</td>
    </tr>
    <tr>
        <td>Memory versus Pointing</td>
        <td>2</td>
        <td>395</td>
    </tr>
    <tr>
        <td>Memory versus Smell</td>
        <td>2</td>
        <td>374</td>
    </tr>
    <tr>
        <td>Navigation Game</td>
        <td>2</td>
        <td>41</td>
    </tr>
    <tr>
        <td>Navigation Learning</td>
        <td>2</td>
        <td>43</td>
    </tr>
    <tr>
        <td>Navigation Warm-up</td>
        <td>2</td>
        <td>43</td>
    </tr>
    <tr>
        <td>Numerosity Warm-Up</td>
        <td>2</td>
        <td>28</td>
    </tr>
    <tr>
        <td>One Cup Warm-up</td>
        <td>2</td>
        <td>388</td>
    </tr>
    <tr>
        <td>Physical Reasoning Game</td>
        <td>2</td>
        <td>252</td>
    </tr>
    <tr>
        <td>Physical Reasoning Warm-up</td>
        <td>2</td>
        <td>290</td>
    </tr>
    <tr>
        <td>Self Control Game</td>
        <td>2</td>
        <td>8</td>
    </tr>
    <tr>
        <td>Shaker Game</td>
        <td>2</td>
        <td>9</td>
    </tr>
    <tr>
        <td>Shaker Warm-Up</td>
        <td>2</td>
        <td>11</td>
    </tr>
    <tr>
        <td>Shared Perspective</td>
        <td>2</td>
        <td>3</td>
    </tr>
    <tr>
        <td>Slide</td>
        <td>2</td>
        <td>12</td>
    </tr>
    <tr>
        <td>Smell Game</td>
        <td>2</td>
        <td>18</td>
    </tr>
    <tr>
        <td>Stair Game</td>
        <td>2</td>
        <td>8</td>
    </tr>
    <tr>
        <td>Switch</td>
        <td>2</td>
        <td>12</td>
    </tr>
    <tr>
        <td>Treat Warm-up</td>
        <td>2</td>
        <td>495</td>
    </tr>
    <tr>
        <td>Turn Your Back</td>
        <td>2</td>
        <td>372</td>
    </tr>
    <tr>
        <td>Two Cup Warm-up</td>
        <td>2</td>
        <td>386</td>
    </tr>
    <tr>
        <td>Warm-up</td>
        <td>2</td>
        <td>77</td>
    </tr>
    <tr>
        <td>Watching</td>
        <td>2</td>
        <td>443</td>
    </tr>
    <tr>
        <td>Watching - Part 2</td>
        <td>2</td>
        <td>372</td>
    </tr>
    <tr>
        <td>Yawn Game</td>
        <td>2</td>
        <td>709</td>
    </tr>
    <tr>
        <td>Yawn Warm-up</td>
        <td>2</td>
        <td>712</td>
    </tr>
    <tr>
        <td>1 vs 1 Game</td>
        <td>3</td>
        <td>22</td>
    </tr>
    <tr>
        <td>3 vs 1 Game</td>
        <td>3</td>
        <td>34</td>
    </tr>
    <tr>
        <td>5 vs 1 Game</td>
        <td>3</td>
        <td>57</td>
    </tr>
    <tr>
        <td>Arm Pointing</td>
        <td>3</td>
        <td>507</td>
    </tr>
    <tr>
        <td>Cover Your Eyes</td>
        <td>3</td>
        <td>416</td>
    </tr>
    <tr>
        <td>Delayed Cup Game</td>
        <td>3</td>
        <td>350</td>
    </tr>
    <tr>
        <td>Different Perspective</td>
        <td>3</td>
        <td>4</td>
    </tr>
    <tr>
        <td>Expression Game</td>
        <td>3</td>
        <td>12</td>
    </tr>
    <tr>
        <td>Eye Contact Game</td>
        <td>3</td>
        <td>589</td>
    </tr>
    <tr>
        <td>Eye Contact Warm-up</td>
        <td>3</td>
        <td>616</td>
    </tr>
    <tr>
        <td>Foot Pointing</td>
        <td>3</td>
        <td>477</td>
    </tr>
    <tr>
        <td>Impossible Task Game</td>
        <td>3</td>
        <td>36</td>
    </tr>
    <tr>
        <td>Impossible Task Warm-up</td>
        <td>3</td>
        <td>37</td>
    </tr>
    <tr>
        <td>Inferential Reasoning Game</td>
        <td>3</td>
        <td>335</td>
    </tr>
    <tr>
        <td>Inferential Reasoning Warm-up</td>
        <td>3</td>
        <td>351</td>
    </tr>
    <tr>
        <td>Memory versus Pointing</td>
        <td>3</td>
        <td>381</td>
    </tr>
    <tr>
        <td>Memory versus Smell</td>
        <td>3</td>
        <td>382</td>
    </tr>
    <tr>
        <td>Navigation Game</td>
        <td>3</td>
        <td>47</td>
    </tr>
    <tr>
        <td>Navigation Learning</td>
        <td>3</td>
        <td>47</td>
    </tr>
    <tr>
        <td>Navigation Warm-up</td>
        <td>3</td>
        <td>50</td>
    </tr>
    <tr>
        <td>Numerosity Warm-Up</td>
        <td>3</td>
        <td>35</td>
    </tr>
    <tr>
        <td>One Cup Warm-up</td>
        <td>3</td>
        <td>388</td>
    </tr>
    <tr>
        <td>Physical Reasoning Game</td>
        <td>3</td>
        <td>321</td>
    </tr>
    <tr>
        <td>Physical Reasoning Warm-up</td>
        <td>3</td>
        <td>337</td>
    </tr>
    <tr>
        <td>Self Control Game</td>
        <td>3</td>
        <td>11</td>
    </tr>
    <tr>
        <td>Shaker Game</td>
        <td>3</td>
        <td>8</td>
    </tr>
    <tr>
        <td>Shaker Warm-Up</td>
        <td>3</td>
        <td>8</td>
    </tr>
    <tr>
        <td>Shared Perspective</td>
        <td>3</td>
        <td>3</td>
    </tr>
    <tr>
        <td>Slide</td>
        <td>3</td>
        <td>16</td>
    </tr>
    <tr>
        <td>Smell Game</td>
        <td>3</td>
        <td>16</td>
    </tr>
    <tr>
        <td>Stair Game</td>
        <td>3</td>
        <td>7</td>
    </tr>
    <tr>
        <td>Switch</td>
        <td>3</td>
        <td>14</td>
    </tr>
    <tr>
        <td>Treat Warm-up</td>
        <td>3</td>
        <td>515</td>
    </tr>
    <tr>
        <td>Turn Your Back</td>
        <td>3</td>
        <td>418</td>
    </tr>
    <tr>
        <td>Two Cup Warm-up</td>
        <td>3</td>
        <td>389</td>
    </tr>
    <tr>
        <td>Warm-Up</td>
        <td>3</td>
        <td>79</td>
    </tr>
    <tr>
        <td>Watching</td>
        <td>3</td>
        <td>472</td>
    </tr>
    <tr>
        <td>Watching - Part 2</td>
        <td>3</td>
        <td>406</td>
    </tr>
    <tr>
        <td>Yawn Game</td>
        <td>3</td>
        <td>681</td>
    </tr>
    <tr>
        <td>Yawn Warm-up</td>
        <td>3</td>
        <td>698</td>
    </tr>
    <tr>
        <td>1 vs 1 Game</td>
        <td>4</td>
        <td>12</td>
    </tr>
    <tr>
        <td>3 vs 1 Game</td>
        <td>4</td>
        <td>16</td>
    </tr>
    <tr>
        <td>5 vs 1 Game</td>
        <td>4</td>
        <td>29</td>
    </tr>
    <tr>
        <td>Arm Pointing</td>
        <td>4</td>
        <td>381</td>
    </tr>
    <tr>
        <td>Cover Your Eyes</td>
        <td>4</td>
        <td>291</td>
    </tr>
    <tr>
        <td>Delayed Cup Game</td>
        <td>4</td>
        <td>256</td>
    </tr>
    <tr>
        <td>Different Perspective</td>
        <td>4</td>
        <td>8</td>
    </tr>
    <tr>
        <td>Expression Game</td>
        <td>4</td>
        <td>10</td>
    </tr>
    <tr>
        <td>Eye Contact Game</td>
        <td>4</td>
        <td>449</td>
    </tr>
    <tr>
        <td>Eye Contact Warm-up</td>
        <td>4</td>
        <td>454</td>
    </tr>
    <tr>
        <td>Foot Pointing</td>
        <td>4</td>
        <td>339</td>
    </tr>
    <tr>
        <td>Impossible Task Game</td>
        <td>4</td>
        <td>43</td>
    </tr>
    <tr>
        <td>Impossible Task Warm-up</td>
        <td>4</td>
        <td>43</td>
    </tr>
    <tr>
        <td>Inferential Reasoning Game</td>
        <td>4</td>
        <td>254</td>
    </tr>
    <tr>
        <td>Inferential Reasoning Warm-up</td>
        <td>4</td>
        <td>257</td>
    </tr>
    <tr>
        <td>Memory versus Pointing</td>
        <td>4</td>
        <td>299</td>
    </tr>
    <tr>
        <td>Memory versus Smell</td>
        <td>4</td>
        <td>280</td>
    </tr>
    <tr>
        <td>Navigation Game</td>
        <td>4</td>
        <td>41</td>
    </tr>
    <tr>
        <td>Navigation Learning</td>
        <td>4</td>
        <td>45</td>
    </tr>
    <tr>
        <td>Navigation Warm-up</td>
        <td>4</td>
        <td>42</td>
    </tr>
    <tr>
        <td>Numerosity Warm-Up</td>
        <td>4</td>
        <td>17</td>
    </tr>
    <tr>
        <td>One Cup Warm-up</td>
        <td>4</td>
        <td>313</td>
    </tr>
    <tr>
        <td>Physical Reasoning Game</td>
        <td>4</td>
        <td>224</td>
    </tr>
    <tr>
        <td>Physical Reasoning Warm-up</td>
        <td>4</td>
        <td>247</td>
    </tr>
    <tr>
        <td>Self Control Game</td>
        <td>4</td>
        <td>9</td>
    </tr>
    <tr>
        <td>Shaker Game</td>
        <td>4</td>
        <td>4</td>
    </tr>
    <tr>
        <td>Shaker Warm-Up</td>
        <td>4</td>
        <td>4</td>
    </tr>
    <tr>
        <td>Shared Perspective</td>
        <td>4</td>
        <td>8</td>
    </tr>
    <tr>
        <td>Slide</td>
        <td>4</td>
        <td>11</td>
    </tr>
    <tr>
        <td>Smell Game</td>
        <td>4</td>
        <td>6</td>
    </tr>
    <tr>
        <td>Stair Game</td>
        <td>4</td>
        <td>4</td>
    </tr>
    <tr>
        <td>Switch</td>
        <td>4</td>
        <td>11</td>
    </tr>
    <tr>
        <td>Treat Warm-up</td>
        <td>4</td>
        <td>393</td>
    </tr>
    <tr>
        <td>Turn Your Back</td>
        <td>4</td>
        <td>298</td>
    </tr>
    <tr>
        <td>Two Cup Warm-up</td>
        <td>4</td>
        <td>308</td>
    </tr>
    <tr>
        <td>Warm-Up</td>
        <td>4</td>
        <td>54</td>
    </tr>
    <tr>
        <td>Watching</td>
        <td>4</td>
        <td>322</td>
    </tr>
    <tr>
        <td>Watching - Part 2</td>
        <td>4</td>
        <td>282</td>
    </tr>
    <tr>
        <td>Yawn Game</td>
        <td>4</td>
        <td>525</td>
    </tr>
    <tr>
        <td>Yawn Warm-up</td>
        <td>4</td>
        <td>541</td>
    </tr>
    <tr>
        <td>1 vs 1 Game</td>
        <td>5</td>
        <td>13</td>
    </tr>
    <tr>
        <td>3 vs 1 Game</td>
        <td>5</td>
        <td>34</td>
    </tr>
    <tr>
        <td>5 vs 1 Game</td>
        <td>5</td>
        <td>50</td>
    </tr>
    <tr>
        <td>Arm Pointing</td>
        <td>5</td>
        <td>1149</td>
    </tr>
    <tr>
        <td>Cover Your Eyes</td>
        <td>5</td>
        <td>753</td>
    </tr>
    <tr>
        <td>Delayed Cup Game</td>
        <td>5</td>
        <td>539</td>
    </tr>
    <tr>
        <td>Different Perspective</td>
        <td>5</td>
        <td>12</td>
    </tr>
    <tr>
        <td>Expression Game</td>
        <td>5</td>
        <td>9</td>
    </tr>
    <tr>
        <td>Eye Contact Game</td>
        <td>5</td>
        <td>1408</td>
    </tr>
    <tr>
        <td>Eye Contact Warm-up</td>
        <td>5</td>
        <td>1636</td>
    </tr>
    <tr>
        <td>Foot Pointing</td>
        <td>5</td>
        <td>926</td>
    </tr>
    <tr>
        <td>Impossible Task Game</td>
        <td>5</td>
        <td>49</td>
    </tr>
    <tr>
        <td>Impossible Task Warm-up</td>
        <td>5</td>
        <td>49</td>
    </tr>
    <tr>
        <td>Inferential Reasoning Game</td>
        <td>5</td>
        <td>533</td>
    </tr>
    <tr>
        <td>Inferential Reasoning Warm-up</td>
        <td>5</td>
        <td>544</td>
    </tr>
    <tr>
        <td>Memory versus Pointing</td>
        <td>5</td>
        <td>711</td>
    </tr>
    <tr>
        <td>Memory versus Smell</td>
        <td>5</td>
        <td>667</td>
    </tr>
    <tr>
        <td>Navigation Game</td>
        <td>5</td>
        <td>336</td>
    </tr>
    <tr>
        <td>Navigation Learning</td>
        <td>5</td>
        <td>444</td>
    </tr>
    <tr>
        <td>Navigation Warm-up</td>
        <td>5</td>
        <td>625</td>
    </tr>
    <tr>
        <td>Numerosity Warm-Up</td>
        <td>5</td>
        <td>37</td>
    </tr>
    <tr>
        <td>One Cup Warm-up</td>
        <td>5</td>
        <td>757</td>
    </tr>
    <tr>
        <td>Physical Reasoning Game</td>
        <td>5</td>
        <td>430</td>
    </tr>
    <tr>
        <td>Physical Reasoning Warm-up</td>
        <td>5</td>
        <td>510</td>
    </tr>
    <tr>
        <td>Self Control Game</td>
        <td>5</td>
        <td>9</td>
    </tr>
    <tr>
        <td>Shaker Game</td>
        <td>5</td>
        <td>10</td>
    </tr>
    <tr>
        <td>Shaker Warm-Up</td>
        <td>5</td>
        <td>10</td>
    </tr>
    <tr>
        <td>Shared Perspective</td>
        <td>5</td>
        <td>11</td>
    </tr>
    <tr>
        <td>Slide</td>
        <td>5</td>
        <td>17</td>
    </tr>
    <tr>
        <td>Smell Game</td>
        <td>5</td>
        <td>19</td>
    </tr>
    <tr>
        <td>Stair Game</td>
        <td>5</td>
        <td>10</td>
    </tr>
    <tr>
        <td>Switch</td>
        <td>5</td>
        <td>15</td>
    </tr>
    <tr>
        <td>Treat Warm-up</td>
        <td>5</td>
        <td>1182</td>
    </tr>
    <tr>
        <td>Turn Your Back</td>
        <td>5</td>
        <td>769</td>
    </tr>
    <tr>
        <td>Two Cup Warm-up</td>
        <td>5</td>
        <td>747</td>
    </tr>
    <tr>
        <td>Warm-Up</td>
        <td>5</td>
        <td>71</td>
    </tr>
    <tr>
        <td>Watching</td>
        <td>5</td>
        <td>980</td>
    </tr>
    <tr>
        <td>Watching - Part 2</td>
        <td>5</td>
        <td>734</td>
    </tr>
    <tr>
        <td>Yawn Game</td>
        <td>5</td>
        <td>2065</td>
    </tr>
    <tr>
        <td>Yawn Warm-up</td>
        <td>5</td>
        <td>2143</td>
    </tr>
    <tr>
        <td>1 vs 1 Game</td>
        <td>6</td>
        <td>18</td>
    </tr>
    <tr>
        <td>3 vs 1 Game</td>
        <td>6</td>
        <td>42</td>
    </tr>
    <tr>
        <td>5 vs 1 Game</td>
        <td>6</td>
        <td>61</td>
    </tr>
    <tr>
        <td>Arm Pointing</td>
        <td>6</td>
        <td>1424</td>
    </tr>
    <tr>
        <td>Cover Your Eyes</td>
        <td>6</td>
        <td>767</td>
    </tr>
    <tr>
        <td>Delayed Cup Game</td>
        <td>6</td>
        <td>525</td>
    </tr>
    <tr>
        <td>Different Perspective</td>
        <td>6</td>
        <td>11</td>
    </tr>
    <tr>
        <td>Expression Game</td>
        <td>6</td>
        <td>11</td>
    </tr>
    <tr>
        <td>Eye Contact Game</td>
        <td>6</td>
        <td>1812</td>
    </tr>
    <tr>
        <td>Eye Contact Warm-up</td>
        <td>6</td>
        <td>2152</td>
    </tr>
    <tr>
        <td>Foot Pointing</td>
        <td>6</td>
        <td>1125</td>
    </tr>
    <tr>
        <td>Impossible Task Game</td>
        <td>6</td>
        <td>59</td>
    </tr>
    <tr>
        <td>Impossible Task Warm-up</td>
        <td>6</td>
        <td>58</td>
    </tr>
    <tr>
        <td>Inferential Reasoning Game</td>
        <td>6</td>
        <td>544</td>
    </tr>
    <tr>
        <td>Inferential Reasoning Warm-up</td>
        <td>6</td>
        <td>550</td>
    </tr>
    <tr>
        <td>Memory versus Pointing</td>
        <td>6</td>
        <td>704</td>
    </tr>
    <tr>
        <td>Memory versus Smell</td>
        <td>6</td>
        <td>666</td>
    </tr>
    <tr>
        <td>Navigation Game</td>
        <td>6</td>
        <td>81</td>
    </tr>
    <tr>
        <td>Navigation Learning</td>
        <td>6</td>
        <td>90</td>
    </tr>
    <tr>
        <td>Navigation Warm-up</td>
        <td>6</td>
        <td>114</td>
    </tr>
    <tr>
        <td>Numerosity Warm-Up</td>
        <td>6</td>
        <td>44</td>
    </tr>
    <tr>
        <td>One Cup Warm-up</td>
        <td>6</td>
        <td>745</td>
    </tr>
    <tr>
        <td>Physical Reasoning Game</td>
        <td>6</td>
        <td>424</td>
    </tr>
    <tr>
        <td>Physical Reasoning Warm-up</td>
        <td>6</td>
        <td>504</td>
    </tr>
    <tr>
        <td>Self Control Game</td>
        <td>6</td>
        <td>11</td>
    </tr>
    <tr>
        <td>Shaker Game</td>
        <td>6</td>
        <td>7</td>
    </tr>
    <tr>
        <td>Shaker Warm-Up</td>
        <td>6</td>
        <td>7</td>
    </tr>
    <tr>
        <td>Shared Perspective</td>
        <td>6</td>
        <td>11</td>
    </tr>
    <tr>
        <td>Slide</td>
        <td>6</td>
        <td>10</td>
    </tr>
    <tr>
        <td>Smell Game</td>
        <td>6</td>
        <td>9</td>
    </tr>
    <tr>
        <td>Stair Game</td>
        <td>6</td>
        <td>7</td>
    </tr>
    <tr>
        <td>Switch</td>
        <td>6</td>
        <td>11</td>
    </tr>
    <tr>
        <td>Treat Warm-up</td>
        <td>6</td>
        <td>1444</td>
    </tr>
    <tr>
        <td>Turn Your Back</td>
        <td>6</td>
        <td>778</td>
    </tr>
    <tr>
        <td>Two Cup Warm-up</td>
        <td>6</td>
        <td>732</td>
    </tr>
    <tr>
        <td>Warm-Up</td>
        <td>6</td>
        <td>64</td>
    </tr>
    <tr>
        <td>Watching</td>
        <td>6</td>
        <td>1035</td>
    </tr>
    <tr>
        <td>Watching - Part 2</td>
        <td>6</td>
        <td>747</td>
    </tr>
    <tr>
        <td>Yawn Game</td>
        <td>6</td>
        <td>2906</td>
    </tr>
    <tr>
        <td>Yawn Warm-up</td>
        <td>6</td>
        <td>3071</td>
    </tr>
    <tr>
        <td>1 vs 1 Game</td>
        <td>7</td>
        <td>36</td>
    </tr>
    <tr>
        <td>3 vs 1 Game</td>
        <td>7</td>
        <td>37</td>
    </tr>
    <tr>
        <td>5 vs 1 Game</td>
        <td>7</td>
        <td>69</td>
    </tr>
    <tr>
        <td>Arm Pointing</td>
        <td>7</td>
        <td>913</td>
    </tr>
    <tr>
        <td>Cover Your Eyes</td>
        <td>7</td>
        <td>521</td>
    </tr>
    <tr>
        <td>Delayed Cup Game</td>
        <td>7</td>
        <td>407</td>
    </tr>
    <tr>
        <td>Different Perspective</td>
        <td>7</td>
        <td>8</td>
    </tr>
    <tr>
        <td>Expression Game</td>
        <td>7</td>
        <td>12</td>
    </tr>
    <tr>
        <td>Eye Contact Game</td>
        <td>7</td>
        <td>1194</td>
    </tr>
    <tr>
        <td>Eye Contact Warm-up</td>
        <td>7</td>
        <td>1379</td>
    </tr>
    <tr>
        <td>Foot Pointing</td>
        <td>7</td>
        <td>759</td>
    </tr>
    <tr>
        <td>Impossible Task Game</td>
        <td>7</td>
        <td>50</td>
    </tr>
    <tr>
        <td>Impossible Task Warm-up</td>
        <td>7</td>
        <td>51</td>
    </tr>
    <tr>
        <td>Inferential Reasoning Game</td>
        <td>7</td>
        <td>432</td>
    </tr>
    <tr>
        <td>Inferential Reasoning Warm-up</td>
        <td>7</td>
        <td>450</td>
    </tr>
    <tr>
        <td>Memory versus Pointing</td>
        <td>7</td>
        <td>511</td>
    </tr>
    <tr>
        <td>Memory versus Smell</td>
        <td>7</td>
        <td>491</td>
    </tr>
    <tr>
        <td>Navigation Game</td>
        <td>7</td>
        <td>70</td>
    </tr>
    <tr>
        <td>Navigation Learning</td>
        <td>7</td>
        <td>74</td>
    </tr>
    <tr>
        <td>Navigation Warm-up</td>
        <td>7</td>
        <td>88</td>
    </tr>
    <tr>
        <td>Numerosity Warm-Up</td>
        <td>7</td>
        <td>37</td>
    </tr>
    <tr>
        <td>One Cup Warm-up</td>
        <td>7</td>
        <td>536</td>
    </tr>
    <tr>
        <td>Physical Reasoning Game</td>
        <td>7</td>
        <td>360</td>
    </tr>
    <tr>
        <td>Physical Reasoning Warm-up</td>
        <td>7</td>
        <td>411</td>
    </tr>
    <tr>
        <td>Self Control Game</td>
        <td>7</td>
        <td>14</td>
    </tr>
    <tr>
        <td>Shaker Game</td>
        <td>7</td>
        <td>5</td>
    </tr>
    <tr>
        <td>Shaker Warm-Up</td>
        <td>7</td>
        <td>5</td>
    </tr>
    <tr>
        <td>Shared Perspective</td>
        <td>7</td>
        <td>7</td>
    </tr>
    <tr>
        <td>Slide</td>
        <td>7</td>
        <td>13</td>
    </tr>
    <tr>
        <td>Smell Game</td>
        <td>7</td>
        <td>21</td>
    </tr>
    <tr>
        <td>Stair Game</td>
        <td>7</td>
        <td>14</td>
    </tr>
    <tr>
        <td>Switch</td>
        <td>7</td>
        <td>11</td>
    </tr>
    <tr>
        <td>Treat Warm-up</td>
        <td>7</td>
        <td>951</td>
    </tr>
    <tr>
        <td>Turn Your Back</td>
        <td>7</td>
        <td>535</td>
    </tr>
    <tr>
        <td>Two Cup Warm-up</td>
        <td>7</td>
        <td>537</td>
    </tr>
    <tr>
        <td>Warm-Up</td>
        <td>7</td>
        <td>101</td>
    </tr>
    <tr>
        <td>Watching</td>
        <td>7</td>
        <td>679</td>
    </tr>
    <tr>
        <td>Watching - Part 2</td>
        <td>7</td>
        <td>504</td>
    </tr>
    <tr>
        <td>Yawn Game</td>
        <td>7</td>
        <td>1775</td>
    </tr>
    <tr>
        <td>Yawn Warm-up</td>
        <td>7</td>
        <td>1909</td>
    </tr>
    <tr>
        <td>1 vs 1 Game</td>
        <td>8</td>
        <td>17</td>
    </tr>
    <tr>
        <td>3 vs 1 Game</td>
        <td>8</td>
        <td>23</td>
    </tr>
    <tr>
        <td>5 vs 1 Game</td>
        <td>8</td>
        <td>38</td>
    </tr>
    <tr>
        <td>Arm Pointing</td>
        <td>8</td>
        <td>779</td>
    </tr>
    <tr>
        <td>Cover Your Eyes</td>
        <td>8</td>
        <td>408</td>
    </tr>
    <tr>
        <td>Delayed Cup Game</td>
        <td>8</td>
        <td>355</td>
    </tr>
    <tr>
        <td>Different Perspective</td>
        <td>8</td>
        <td>10</td>
    </tr>
    <tr>
        <td>Expression Game</td>
        <td>8</td>
        <td>11</td>
    </tr>
    <tr>
        <td>Eye Contact Game</td>
        <td>8</td>
        <td>1130</td>
    </tr>
    <tr>
        <td>Eye Contact Warm-up</td>
        <td>8</td>
        <td>1256</td>
    </tr>
    <tr>
        <td>Foot Pointing</td>
        <td>8</td>
        <td>653</td>
    </tr>
    <tr>
        <td>Impossible Task Game</td>
        <td>8</td>
        <td>32</td>
    </tr>
    <tr>
        <td>Impossible Task Warm-up</td>
        <td>8</td>
        <td>34</td>
    </tr>
    <tr>
        <td>Inferential Reasoning Game</td>
        <td>8</td>
        <td>350</td>
    </tr>
    <tr>
        <td>Inferential Reasoning Warm-up</td>
        <td>8</td>
        <td>354</td>
    </tr>
    <tr>
        <td>Memory versus Pointing</td>
        <td>8</td>
        <td>415</td>
    </tr>
    <tr>
        <td>Memory versus Smell</td>
        <td>8</td>
        <td>402</td>
    </tr>
    <tr>
        <td>Navigation Game</td>
        <td>8</td>
        <td>41</td>
    </tr>
    <tr>
        <td>Navigation Learning</td>
        <td>8</td>
        <td>34</td>
    </tr>
    <tr>
        <td>Navigation Warm-up</td>
        <td>8</td>
        <td>40</td>
    </tr>
    <tr>
        <td>Numerosity Warm-Up</td>
        <td>8</td>
        <td>23</td>
    </tr>
    <tr>
        <td>One Cup Warm-up</td>
        <td>8</td>
        <td>416</td>
    </tr>
    <tr>
        <td>Physical Reasoning Game</td>
        <td>8</td>
        <td>316</td>
    </tr>
    <tr>
        <td>Physical Reasoning Warm-up</td>
        <td>8</td>
        <td>347</td>
    </tr>
    <tr>
        <td>Self Control Game</td>
        <td>8</td>
        <td>13</td>
    </tr>
    <tr>
        <td>Shaker Game</td>
        <td>8</td>
        <td>6</td>
    </tr>
    <tr>
        <td>Shaker Warm-Up</td>
        <td>8</td>
        <td>6</td>
    </tr>
    <tr>
        <td>Shared Perspective</td>
        <td>8</td>
        <td>10</td>
    </tr>
    <tr>
        <td>Slide</td>
        <td>8</td>
        <td>6</td>
    </tr>
    <tr>
        <td>Smell Game</td>
        <td>8</td>
        <td>10</td>
    </tr>
    <tr>
        <td>Stair Game</td>
        <td>8</td>
        <td>15</td>
    </tr>
    <tr>
        <td>Switch</td>
        <td>8</td>
        <td>10</td>
    </tr>
    <tr>
        <td>Treat Warm-up</td>
        <td>8</td>
        <td>791</td>
    </tr>
    <tr>
        <td>Turn Your Back</td>
        <td>8</td>
        <td>418</td>
    </tr>
    <tr>
        <td>Two Cup Warm-up</td>
        <td>8</td>
        <td>419</td>
    </tr>
    <tr>
        <td>Warm-Up</td>
        <td>8</td>
        <td>64</td>
    </tr>
    <tr>
        <td>Watching</td>
        <td>8</td>
        <td>511</td>
    </tr>
    <tr>
        <td>Watching - Part 2</td>
        <td>8</td>
        <td>405</td>
    </tr>
    <tr>
        <td>Yawn Game</td>
        <td>8</td>
        <td>1520</td>
    </tr>
    <tr>
        <td>Yawn Warm-up</td>
        <td>8</td>
        <td>1694</td>
    </tr>
    <tr>
        <td>1 vs 1 Game</td>
        <td>9</td>
        <td>28</td>
    </tr>
    <tr>
        <td>3 vs 1 Game</td>
        <td>9</td>
        <td>24</td>
    </tr>
    <tr>
        <td>5 vs 1 Game</td>
        <td>9</td>
        <td>50</td>
    </tr>
    <tr>
        <td>Arm Pointing</td>
        <td>9</td>
        <td>1243</td>
    </tr>
    <tr>
        <td>Cover Your Eyes</td>
        <td>9</td>
        <td>574</td>
    </tr>
    <tr>
        <td>Delayed Cup Game</td>
        <td>9</td>
        <td>424</td>
    </tr>
    <tr>
        <td>Different Perspective</td>
        <td>9</td>
        <td>12</td>
    </tr>
    <tr>
        <td>Expression Game</td>
        <td>9</td>
        <td>17</td>
    </tr>
    <tr>
        <td>Eye Contact Game</td>
        <td>9</td>
        <td>1674</td>
    </tr>
    <tr>
        <td>Eye Contact Warm-up</td>
        <td>9</td>
        <td>1967</td>
    </tr>
    <tr>
        <td>Foot Pointing</td>
        <td>9</td>
        <td>992</td>
    </tr>
    <tr>
        <td>Impossible Task Game</td>
        <td>9</td>
        <td>35</td>
    </tr>
    <tr>
        <td>Impossible Task Warm-up</td>
        <td>9</td>
        <td>36</td>
    </tr>
    <tr>
        <td>Inferential Reasoning Game</td>
        <td>9</td>
        <td>398</td>
    </tr>
    <tr>
        <td>Inferential Reasoning Warm-up</td>
        <td>9</td>
        <td>399</td>
    </tr>
    <tr>
        <td>Memory versus Pointing</td>
        <td>9</td>
        <td>574</td>
    </tr>
    <tr>
        <td>Memory versus Smell</td>
        <td>9</td>
        <td>529</td>
    </tr>
    <tr>
        <td>Navigation Game</td>
        <td>9</td>
        <td>52</td>
    </tr>
    <tr>
        <td>Navigation Learning</td>
        <td>9</td>
        <td>54</td>
    </tr>
    <tr>
        <td>Navigation Warm-up</td>
        <td>9</td>
        <td>58</td>
    </tr>
    <tr>
        <td>Numerosity Warm-Up</td>
        <td>9</td>
        <td>24</td>
    </tr>
    <tr>
        <td>One Cup Warm-up</td>
        <td>9</td>
        <td>602</td>
    </tr>
    <tr>
        <td>Physical Reasoning Game</td>
        <td>9</td>
        <td>309</td>
    </tr>
    <tr>
        <td>Physical Reasoning Warm-up</td>
        <td>9</td>
        <td>364</td>
    </tr>
    <tr>
        <td>Self Control Game</td>
        <td>9</td>
        <td>19</td>
    </tr>
    <tr>
        <td>Shaker Game</td>
        <td>9</td>
        <td>12</td>
    </tr>
    <tr>
        <td>Shaker Warm-Up</td>
        <td>9</td>
        <td>13</td>
    </tr>
    <tr>
        <td>Shared Perspective</td>
        <td>9</td>
        <td>12</td>
    </tr>
    <tr>
        <td>Slide</td>
        <td>9</td>
        <td>18</td>
    </tr>
    <tr>
        <td>Smell Game</td>
        <td>9</td>
        <td>16</td>
    </tr>
    <tr>
        <td>Stair Game</td>
        <td>9</td>
        <td>17</td>
    </tr>
    <tr>
        <td>Switch</td>
        <td>9</td>
        <td>13</td>
    </tr>
    <tr>
        <td>Treat Warm-up</td>
        <td>9</td>
        <td>1303</td>
    </tr>
    <tr>
        <td>Turn Your Back</td>
        <td>9</td>
        <td>599</td>
    </tr>
    <tr>
        <td>Two Cup Warm-up</td>
        <td>9</td>
        <td>578</td>
    </tr>
    <tr>
        <td>Warm-Up</td>
        <td>9</td>
        <td>103</td>
    </tr>
    <tr>
        <td>Watching</td>
        <td>9</td>
        <td>809</td>
    </tr>
    <tr>
        <td>Watching - Part 2</td>
        <td>9</td>
        <td>568</td>
    </tr>
    <tr>
        <td>Yawn Game</td>
        <td>9</td>
        <td>2563</td>
    </tr>
    <tr>
        <td>Yawn Warm-up</td>
        <td>9</td>
        <td>2771</td>
    </tr>
    <tr>
        <td>1 vs 1 Game</td>
        <td>10</td>
        <td>27</td>
    </tr>
    <tr>
        <td>3 vs 1 Game</td>
        <td>10</td>
        <td>28</td>
    </tr>
    <tr>
        <td>5 vs 1 Game</td>
        <td>10</td>
        <td>54</td>
    </tr>
    <tr>
        <td>Arm Pointing</td>
        <td>10</td>
        <td>2535</td>
    </tr>
    <tr>
        <td>Cover Your Eyes</td>
        <td>10</td>
        <td>1653</td>
    </tr>
    <tr>
        <td>Delayed Cup Game</td>
        <td>10</td>
        <td>1019</td>
    </tr>
    <tr>
        <td>Different Perspective</td>
        <td>10</td>
        <td>4</td>
    </tr>
    <tr>
        <td>Expression Game</td>
        <td>10</td>
        <td>3</td>
    </tr>
    <tr>
        <td>Eye Contact Game</td>
        <td>10</td>
        <td>3452</td>
    </tr>
    <tr>
        <td>Eye Contact Warm-up</td>
        <td>10</td>
        <td>3675</td>
    </tr>
    <tr>
        <td>Foot Pointing</td>
        <td>10</td>
        <td>2290</td>
    </tr>
    <tr>
        <td>Impossible Task Game</td>
        <td>10</td>
        <td>37</td>
    </tr>
    <tr>
        <td>Impossible Task Warm-up</td>
        <td>10</td>
        <td>36</td>
    </tr>
    <tr>
        <td>Inferential Reasoning Game</td>
        <td>10</td>
        <td>785</td>
    </tr>
    <tr>
        <td>Inferential Reasoning Warm-up</td>
        <td>10</td>
        <td>794</td>
    </tr>
    <tr>
        <td>Memory versus Pointing</td>
        <td>10</td>
        <td>1218</td>
    </tr>
    <tr>
        <td>Memory versus Smell</td>
        <td>10</td>
        <td>1111</td>
    </tr>
    <tr>
        <td>Navigation Game</td>
        <td>10</td>
        <td>69</td>
    </tr>
    <tr>
        <td>Navigation Learning</td>
        <td>10</td>
        <td>70</td>
    </tr>
    <tr>
        <td>Navigation Warm-up</td>
        <td>10</td>
        <td>76</td>
    </tr>
    <tr>
        <td>Numerosity Warm-Up</td>
        <td>10</td>
        <td>29</td>
    </tr>
    <tr>
        <td>One Cup Warm-up</td>
        <td>10</td>
        <td>1272</td>
    </tr>
    <tr>
        <td>Physical Reasoning Game</td>
        <td>10</td>
        <td>711</td>
    </tr>
    <tr>
        <td>Physical Reasoning Warm-up</td>
        <td>10</td>
        <td>742</td>
    </tr>
    <tr>
        <td>Self Control Game</td>
        <td>10</td>
        <td>9</td>
    </tr>
    <tr>
        <td>Shaker Game</td>
        <td>10</td>
        <td>10</td>
    </tr>
    <tr>
        <td>Shaker Warm-Up</td>
        <td>10</td>
        <td>11</td>
    </tr>
    <tr>
        <td>Shared Perspective</td>
        <td>10</td>
        <td>4</td>
    </tr>
    <tr>
        <td>Slide</td>
        <td>10</td>
        <td>7</td>
    </tr>
    <tr>
        <td>Smell Game</td>
        <td>10</td>
        <td>15</td>
    </tr>
    <tr>
        <td>Stair Game</td>
        <td>10</td>
        <td>7</td>
    </tr>
    <tr>
        <td>Switch</td>
        <td>10</td>
        <td>9</td>
    </tr>
    <tr>
        <td>Treat Warm-up</td>
        <td>10</td>
        <td>2626</td>
    </tr>
    <tr>
        <td>Turn Your Back</td>
        <td>10</td>
        <td>1711</td>
    </tr>
    <tr>
        <td>Two Cup Warm-up</td>
        <td>10</td>
        <td>1234</td>
    </tr>
    <tr>
        <td>Warm-up</td>
        <td>10</td>
        <td>69</td>
    </tr>
    <tr>
        <td>Watching</td>
        <td>10</td>
        <td>1797</td>
    </tr>
    <tr>
        <td>Watching - Part 2</td>
        <td>10</td>
        <td>1578</td>
    </tr>
    <tr>
        <td>Yawn Game</td>
        <td>10</td>
        <td>4073</td>
    </tr>
    <tr>
        <td>Yawn Warm-up</td>
        <td>10</td>
        <td>4387</td>
    </tr>
    <tr>
        <td>1 vs 1 Game</td>
        <td>11</td>
        <td>15</td>
    </tr>
    <tr>
        <td>3 vs 1 Game</td>
        <td>11</td>
        <td>22</td>
    </tr>
    <tr>
        <td>5 vs 1 Game</td>
        <td>11</td>
        <td>40</td>
    </tr>
    <tr>
        <td>Arm Pointing</td>
        <td>11</td>
        <td>735</td>
    </tr>
    <tr>
        <td>Cover Your Eyes</td>
        <td>11</td>
        <td>595</td>
    </tr>
    <tr>
        <td>Delayed Cup Game</td>
        <td>11</td>
        <td>422</td>
    </tr>
    <tr>
        <td>Different Perspective</td>
        <td>11</td>
        <td>6</td>
    </tr>
    <tr>
        <td>Expression Game</td>
        <td>11</td>
        <td>11</td>
    </tr>
    <tr>
        <td>Eye Contact Game</td>
        <td>11</td>
        <td>889</td>
    </tr>
    <tr>
        <td>Eye Contact Warm-up</td>
        <td>11</td>
        <td>941</td>
    </tr>
    <tr>
        <td>Foot Pointing</td>
        <td>11</td>
        <td>685</td>
    </tr>
    <tr>
        <td>Impossible Task Game</td>
        <td>11</td>
        <td>48</td>
    </tr>
    <tr>
        <td>Impossible Task Warm-up</td>
        <td>11</td>
        <td>49</td>
    </tr>
    <tr>
        <td>Inferential Reasoning Game</td>
        <td>11</td>
        <td>362</td>
    </tr>
    <tr>
        <td>Inferential Reasoning Warm-up</td>
        <td>11</td>
        <td>376</td>
    </tr>
    <tr>
        <td>Memory versus Pointing</td>
        <td>11</td>
        <td>477</td>
    </tr>
    <tr>
        <td>Memory versus Smell</td>
        <td>11</td>
        <td>444</td>
    </tr>
    <tr>
        <td>Navigation Game</td>
        <td>11</td>
        <td>47</td>
    </tr>
    <tr>
        <td>Navigation Learning</td>
        <td>11</td>
        <td>47</td>
    </tr>
    <tr>
        <td>Navigation Warm-up</td>
        <td>11</td>
        <td>52</td>
    </tr>
    <tr>
        <td>Numerosity Warm-Up</td>
        <td>11</td>
        <td>26</td>
    </tr>
    <tr>
        <td>One Cup Warm-up</td>
        <td>11</td>
        <td>491</td>
    </tr>
    <tr>
        <td>Physical Reasoning Game</td>
        <td>11</td>
        <td>341</td>
    </tr>
    <tr>
        <td>Physical Reasoning Warm-up</td>
        <td>11</td>
        <td>349</td>
    </tr>
    <tr>
        <td>Self Control Game</td>
        <td>11</td>
        <td>15</td>
    </tr>
    <tr>
        <td>Shaker Game</td>
        <td>11</td>
        <td>3</td>
    </tr>
    <tr>
        <td>Shaker Warm-Up</td>
        <td>11</td>
        <td>3</td>
    </tr>
    <tr>
        <td>Shared Perspective</td>
        <td>11</td>
        <td>6</td>
    </tr>
    <tr>
        <td>Slide</td>
        <td>11</td>
        <td>13</td>
    </tr>
    <tr>
        <td>Smell Game</td>
        <td>11</td>
        <td>12</td>
    </tr>
    <tr>
        <td>Stair Game</td>
        <td>11</td>
        <td>3</td>
    </tr>
    <tr>
        <td>Switch</td>
        <td>11</td>
        <td>10</td>
    </tr>
    <tr>
        <td>Treat Warm-up</td>
        <td>11</td>
        <td>744</td>
    </tr>
    <tr>
        <td>Turn Your Back</td>
        <td>11</td>
        <td>601</td>
    </tr>
    <tr>
        <td>Two Cup Warm-up</td>
        <td>11</td>
        <td>482</td>
    </tr>
    <tr>
        <td>Warm-Up</td>
        <td>11</td>
        <td>65</td>
    </tr>
    <tr>
        <td>Watching</td>
        <td>11</td>
        <td>611</td>
    </tr>
    <tr>
        <td>Watching - Part 2</td>
        <td>11</td>
        <td>565</td>
    </tr>
    <tr>
        <td>Yawn Game</td>
        <td>11</td>
        <td>989</td>
    </tr>
    <tr>
        <td>Yawn Warm-up</td>
        <td>11</td>
        <td>1060</td>
    </tr>
    <tr>
        <td>1 vs 1 Game</td>
        <td>12</td>
        <td>14</td>
    </tr>
    <tr>
        <td>3 vs 1 Game</td>
        <td>12</td>
        <td>45</td>
    </tr>
    <tr>
        <td>5 vs 1 Game</td>
        <td>12</td>
        <td>59</td>
    </tr>
    <tr>
        <td>Arm Pointing</td>
        <td>12</td>
        <td>666</td>
    </tr>
    <tr>
        <td>Cover Your Eyes</td>
        <td>12</td>
        <td>447</td>
    </tr>
    <tr>
        <td>Delayed Cup Game</td>
        <td>12</td>
        <td>299</td>
    </tr>
    <tr>
        <td>Different Perspective</td>
        <td>12</td>
        <td>9</td>
    </tr>
    <tr>
        <td>Expression Game</td>
        <td>12</td>
        <td>13</td>
    </tr>
    <tr>
        <td>Eye Contact Game</td>
        <td>12</td>
        <td>760</td>
    </tr>
    <tr>
        <td>Eye Contact Warm-up</td>
        <td>12</td>
        <td>839</td>
    </tr>
    <tr>
        <td>Foot Pointing</td>
        <td>12</td>
        <td>566</td>
    </tr>
    <tr>
        <td>Impossible Task Game</td>
        <td>12</td>
        <td>46</td>
    </tr>
    <tr>
        <td>Impossible Task Warm-up</td>
        <td>12</td>
        <td>46</td>
    </tr>
    <tr>
        <td>Inferential Reasoning Game</td>
        <td>12</td>
        <td>280</td>
    </tr>
    <tr>
        <td>Inferential Reasoning Warm-up</td>
        <td>12</td>
        <td>296</td>
    </tr>
    <tr>
        <td>Memory versus Pointing</td>
        <td>12</td>
        <td>376</td>
    </tr>
    <tr>
        <td>Memory versus Smell</td>
        <td>12</td>
        <td>352</td>
    </tr>
    <tr>
        <td>Navigation Game</td>
        <td>12</td>
        <td>45</td>
    </tr>
    <tr>
        <td>Navigation Learning</td>
        <td>12</td>
        <td>47</td>
    </tr>
    <tr>
        <td>Navigation Warm-up</td>
        <td>12</td>
        <td>49</td>
    </tr>
    <tr>
        <td>Numerosity Warm-Up</td>
        <td>12</td>
        <td>46</td>
    </tr>
    <tr>
        <td>One Cup Warm-up</td>
        <td>12</td>
        <td>401</td>
    </tr>
    <tr>
        <td>Physical Reasoning Game</td>
        <td>12</td>
        <td>250</td>
    </tr>
    <tr>
        <td>Physical Reasoning Warm-up</td>
        <td>12</td>
        <td>276</td>
    </tr>
    <tr>
        <td>Self Control Game</td>
        <td>12</td>
        <td>6</td>
    </tr>
    <tr>
        <td>Shaker Game</td>
        <td>12</td>
        <td>1</td>
    </tr>
    <tr>
        <td>Shaker Warm-Up</td>
        <td>12</td>
        <td>1</td>
    </tr>
    <tr>
        <td>Shared Perspective</td>
        <td>12</td>
        <td>7</td>
    </tr>
    <tr>
        <td>Slide</td>
        <td>12</td>
        <td>7</td>
    </tr>
    <tr>
        <td>Smell Game</td>
        <td>12</td>
        <td>13</td>
    </tr>
    <tr>
        <td>Stair Game</td>
        <td>12</td>
        <td>8</td>
    </tr>
    <tr>
        <td>Switch</td>
        <td>12</td>
        <td>6</td>
    </tr>
    <tr>
        <td>Treat Warm-up</td>
        <td>12</td>
        <td>667</td>
    </tr>
    <tr>
        <td>Turn Your Back</td>
        <td>12</td>
        <td>467</td>
    </tr>
    <tr>
        <td>Two Cup Warm-up</td>
        <td>12</td>
        <td>379</td>
    </tr>
    <tr>
        <td>Warm-up</td>
        <td>12</td>
        <td>56</td>
    </tr>
    <tr>
        <td>Watching</td>
        <td>12</td>
        <td>555</td>
    </tr>
    <tr>
        <td>Watching - Part 2</td>
        <td>12</td>
        <td>438</td>
    </tr>
    <tr>
        <td>Yawn Game</td>
        <td>12</td>
        <td>978</td>
    </tr>
    <tr>
        <td>Yawn Warm-up</td>
        <td>12</td>
        <td>1043</td>
    </tr>
</table>



Notice that in the first case, the first block of rows share the same test_name, but are broken up into separate months (for those of you who took the "Data Visualization and Communication with Tableau" course of this specialization, this is similar to what would happen if you put test_name first and created_at second on the rows or columns shelf in Tableau).  

In the second case, the first block of rows share the same month, but are broken up into separate tests  (this is similar to what would happen if you put created_at first and test_name second on the rows or columns shelf in Tableau).  If you were to visualize these outputs, they would look like the charts below.

<img src="https://duke.box.com/shared/static/y6l3ldxg289brid5mmn886qweglt65qv.jpg" width=800 alt="ORDER" />

Different database servers might default to ordering the outputs in a certain way, but you shouldn't rely on that being the case.  To ensure the output is ordered in a way you intend, add an ORDER BY clause to your grouped query using the syntax you already know and have practiced:

```mySQL
SELECT test_name, MONTH(created_at) AS Month, COUNT(created_at) AS Num_Completed_Tests
FROM complete_tests
GROUP BY test_name, Month
ORDER BY test_name ASC, Month ASC;
```

**Question 1: Output a table that calculates the number of distinct female and male dogs in each breed group of the Dogs table, sorted by the total number of dogs in descending order (the sex/breed_group pair with the greatest number of dogs should have 8466 unique Dog_Guids):**


```python
%%sql
SELECT * 
FROM dogs
LIMIT 1;
```

    1 rows affected.





<table>
    <tr>
        <th>gender</th>
        <th>birthday</th>
        <th>breed</th>
        <th>weight</th>
        <th>dog_fixed</th>
        <th>dna_tested</th>
        <th>created_at</th>
        <th>updated_at</th>
        <th>dimension</th>
        <th>exclude</th>
        <th>breed_type</th>
        <th>breed_group</th>
        <th>dog_guid</th>
        <th>user_guid</th>
        <th>total_tests_completed</th>
        <th>mean_iti_days</th>
        <th>mean_iti_minutes</th>
        <th>median_iti_days</th>
        <th>median_iti_minutes</th>
        <th>time_diff_between_first_and_last_game_days</th>
        <th>time_diff_between_first_and_last_game_minutes</th>
    </tr>
    <tr>
        <td>female</td>
        <td>2011</td>
        <td>Labrador Retriever</td>
        <td>50</td>
        <td>1</td>
        <td>0</td>
        <td>2013-02-05 03:57:19</td>
        <td>2013-07-25 19:41:49</td>
        <td>charmer</td>
        <td>None</td>
        <td>Pure Breed</td>
        <td>Sporting</td>
        <td>fd27b272-7144-11e5-ba71-058fbc01cf0b</td>
        <td>ce134e42-7144-11e5-ba71-058fbc01cf0b</td>
        <td>21</td>
        <td>28.20107581</td>
        <td>40609.549167</td>
        <td>0.004687499952</td>
        <td>6.7499999308</td>
        <td>564.0215162</td>
        <td>812190.98333</td>
    </tr>
</table>




```python
%%sql
SELECT gender, breed_group, COUNT(DISTINCT dog_guid) AS dog
FROM dogs
GROUP BY breed_group, gender
ORDER BY dog DESC;
```

    18 rows affected.





<table>
    <tr>
        <th>gender</th>
        <th>breed_group</th>
        <th>dog</th>
    </tr>
    <tr>
        <td>male</td>
        <td>None</td>
        <td>8466</td>
    </tr>
    <tr>
        <td>female</td>
        <td>None</td>
        <td>8367</td>
    </tr>
    <tr>
        <td>male</td>
        <td>Sporting</td>
        <td>2584</td>
    </tr>
    <tr>
        <td>female</td>
        <td>Sporting</td>
        <td>2262</td>
    </tr>
    <tr>
        <td>male</td>
        <td>Herding</td>
        <td>1736</td>
    </tr>
    <tr>
        <td>female</td>
        <td>Herding</td>
        <td>1704</td>
    </tr>
    <tr>
        <td>male</td>
        <td>Toy</td>
        <td>1473</td>
    </tr>
    <tr>
        <td>female</td>
        <td>Toy</td>
        <td>1145</td>
    </tr>
    <tr>
        <td>male</td>
        <td>Non-Sporting</td>
        <td>1098</td>
    </tr>
    <tr>
        <td>male</td>
        <td>Working</td>
        <td>1075</td>
    </tr>
    <tr>
        <td>female</td>
        <td>Non-Sporting</td>
        <td>919</td>
    </tr>
    <tr>
        <td>male</td>
        <td>Terrier</td>
        <td>919</td>
    </tr>
    <tr>
        <td>female</td>
        <td>Working</td>
        <td>895</td>
    </tr>
    <tr>
        <td>female</td>
        <td>Terrier</td>
        <td>794</td>
    </tr>
    <tr>
        <td>male</td>
        <td>Hound</td>
        <td>725</td>
    </tr>
    <tr>
        <td>female</td>
        <td>Hound</td>
        <td>614</td>
    </tr>
    <tr>
        <td>male</td>
        <td></td>
        <td>147</td>
    </tr>
    <tr>
        <td>female</td>
        <td></td>
        <td>127</td>
    </tr>
</table>



Some database servers, including MySQL, allow you to use numbers in place of field names in the GROUP BY or ORDER BY fields to reduce the overall length of the queries.  I tend to avoid this abbreviated method of writing queries because I find it challenging to troubleshoot when you are writing complicated queries with many fields, but it does allow you to write queries faster.  To use this method, assign each field in your SELECT statement a number acording to the order the field appears in the SELECT statement.  In the following statement:

```mySQL
SELECT test_name, MONTH(created_at) AS Month, COUNT(created_at) AS Num_Completed_Tests
```

test_name would be #1, Month would be #2, and Num_Completed_Tests would be #3.  You could then rewrite the query above to read:

```mySQL
SELECT test_name, MONTH(created_at) AS Month, COUNT(created_at) AS Num_Completed_Tests
FROM complete_tests
GROUP BY 1, 2
ORDER BY 1 ASC, 2 ASC;
```

**Question 2: Revise the query your wrote in Question 1 so that it uses only numbers in the GROUP BY and ORDER BY fields.**


```python
%%sql
SELECT gender, breed_group, COUNT(DISTINCT dog_guid) AS dog
FROM dogs
GROUP BY 2, 1
ORDER BY 3 DESC;
```

    18 rows affected.





<table>
    <tr>
        <th>gender</th>
        <th>breed_group</th>
        <th>dog</th>
    </tr>
    <tr>
        <td>male</td>
        <td>None</td>
        <td>8466</td>
    </tr>
    <tr>
        <td>female</td>
        <td>None</td>
        <td>8367</td>
    </tr>
    <tr>
        <td>male</td>
        <td>Sporting</td>
        <td>2584</td>
    </tr>
    <tr>
        <td>female</td>
        <td>Sporting</td>
        <td>2262</td>
    </tr>
    <tr>
        <td>male</td>
        <td>Herding</td>
        <td>1736</td>
    </tr>
    <tr>
        <td>female</td>
        <td>Herding</td>
        <td>1704</td>
    </tr>
    <tr>
        <td>male</td>
        <td>Toy</td>
        <td>1473</td>
    </tr>
    <tr>
        <td>female</td>
        <td>Toy</td>
        <td>1145</td>
    </tr>
    <tr>
        <td>male</td>
        <td>Non-Sporting</td>
        <td>1098</td>
    </tr>
    <tr>
        <td>male</td>
        <td>Working</td>
        <td>1075</td>
    </tr>
    <tr>
        <td>female</td>
        <td>Non-Sporting</td>
        <td>919</td>
    </tr>
    <tr>
        <td>male</td>
        <td>Terrier</td>
        <td>919</td>
    </tr>
    <tr>
        <td>female</td>
        <td>Working</td>
        <td>895</td>
    </tr>
    <tr>
        <td>female</td>
        <td>Terrier</td>
        <td>794</td>
    </tr>
    <tr>
        <td>male</td>
        <td>Hound</td>
        <td>725</td>
    </tr>
    <tr>
        <td>female</td>
        <td>Hound</td>
        <td>614</td>
    </tr>
    <tr>
        <td>male</td>
        <td></td>
        <td>147</td>
    </tr>
    <tr>
        <td>female</td>
        <td></td>
        <td>127</td>
    </tr>
</table>



## The HAVING clause

Just like you can query subsets of rows using the WHERE clause, you can query subsets of aggregated groups using the HAVING clause.  However, wheras the expression that follows a WHERE clause has to be applicable to each row of data in a column, the expression that follows a HAVING clause has to be applicable or computable using a group of data.  

If you wanted to examine the number of tests completed only during the winter holiday months of November and December, you would need to use a WHERE clause, because the month a test was completed in is recorded in each row.  Your query might look like this:

```mySQL
SELECT test_name, MONTH(created_at) AS Month, COUNT(created_at) AS Num_Completed_Tests
FROM complete_tests
WHERE MONTH(created_at)=11 OR MONTH(created_at)=12
GROUP BY 1, 2
ORDER BY 3 DESC;
```
If you then wanted to output only the test-month pairs that had at least 20 records in them, you would add a HAVING clause, because the stipulation of at least 20 records only makes sense and is only computable at the aggregated group level:

```mySQL
SELECT test_name, MONTH(created_at) AS Month, COUNT(created_at) AS Num_Completed_Tests
FROM complete_tests
WHERE MONTH(created_at)=11 OR MONTH(created_at)=12
GROUP BY 1, 2
HAVING COUNT(created_at)>=20
ORDER BY 3 DESC;
```

**Question 3: Revise the query your wrote in Question 2 so that it (1) excludes the NULL and empty string entries in the breed_group field, and (2) excludes any groups that don't have at least 1,000 distinct Dog_Guids in them.  Your result should contain 8 rows.  (HINT: sometimes empty strings are registered as non-NULL values.  You might want to include the following line somewhere in your query to exclude these values as well):**

```mySQL
breed_group!=""
```



```python
%%sql
SELECT gender, breed_group, COUNT(DISTINCT dog_guid) AS dog
FROM dogs
WHERE breed_group IS NOT NULL AND breed_group!=""
GROUP BY 2, 1
HAVING dog > 999
ORDER BY 3 DESC;
```

    8 rows affected.





<table>
    <tr>
        <th>gender</th>
        <th>breed_group</th>
        <th>dog</th>
    </tr>
    <tr>
        <td>male</td>
        <td>Sporting</td>
        <td>2584</td>
    </tr>
    <tr>
        <td>female</td>
        <td>Sporting</td>
        <td>2262</td>
    </tr>
    <tr>
        <td>male</td>
        <td>Herding</td>
        <td>1736</td>
    </tr>
    <tr>
        <td>female</td>
        <td>Herding</td>
        <td>1704</td>
    </tr>
    <tr>
        <td>male</td>
        <td>Toy</td>
        <td>1473</td>
    </tr>
    <tr>
        <td>female</td>
        <td>Toy</td>
        <td>1145</td>
    </tr>
    <tr>
        <td>male</td>
        <td>Non-Sporting</td>
        <td>1098</td>
    </tr>
    <tr>
        <td>male</td>
        <td>Working</td>
        <td>1075</td>
    </tr>
</table>



We will review several issues that can be tricky about using GROUP BY in your queries in the next lesson, but those issues will make more sense once you are sure you are comfortable with the basic functionality of the GROUP BY and HAVING clauses.  
   
      

## Practice incorporating GROUP BY and HAVING into your own queries.

**Question 4: Write a query that outputs the average number of tests completed and average mean inter-test-interval for every breed type, sorted by the average number of completed tests in descending order (popular hybrid should be the first row in your output).**


```python
%%sql
SHOW tables;
```

    6 rows affected.





<table>
    <tr>
        <th>Tables_in_dognitiondb</th>
    </tr>
    <tr>
        <td>complete_tests</td>
    </tr>
    <tr>
        <td>dogs</td>
    </tr>
    <tr>
        <td>exam_answers</td>
    </tr>
    <tr>
        <td>reviews</td>
    </tr>
    <tr>
        <td>site_activities</td>
    </tr>
    <tr>
        <td>users</td>
    </tr>
</table>




```python
%%sql
SELECT *
FROM dogs
LIMIT 5;
```

    5 rows affected.





<table>
    <tr>
        <th>gender</th>
        <th>birthday</th>
        <th>breed</th>
        <th>weight</th>
        <th>dog_fixed</th>
        <th>dna_tested</th>
        <th>created_at</th>
        <th>updated_at</th>
        <th>dimension</th>
        <th>exclude</th>
        <th>breed_type</th>
        <th>breed_group</th>
        <th>dog_guid</th>
        <th>user_guid</th>
        <th>total_tests_completed</th>
        <th>mean_iti_days</th>
        <th>mean_iti_minutes</th>
        <th>median_iti_days</th>
        <th>median_iti_minutes</th>
        <th>time_diff_between_first_and_last_game_days</th>
        <th>time_diff_between_first_and_last_game_minutes</th>
    </tr>
    <tr>
        <td>female</td>
        <td>2011</td>
        <td>Labrador Retriever</td>
        <td>50</td>
        <td>1</td>
        <td>0</td>
        <td>2013-02-05 03:57:19</td>
        <td>2013-07-25 19:41:49</td>
        <td>charmer</td>
        <td>None</td>
        <td>Pure Breed</td>
        <td>Sporting</td>
        <td>fd27b272-7144-11e5-ba71-058fbc01cf0b</td>
        <td>ce134e42-7144-11e5-ba71-058fbc01cf0b</td>
        <td>21</td>
        <td>28.20107581</td>
        <td>40609.549167</td>
        <td>0.004687499952</td>
        <td>6.7499999308</td>
        <td>564.0215162</td>
        <td>812190.98333</td>
    </tr>
    <tr>
        <td>male</td>
        <td>2007</td>
        <td>Shetland Sheepdog</td>
        <td>20</td>
        <td>1</td>
        <td>0</td>
        <td>2013-02-05 15:35:09</td>
        <td>2013-07-25 19:41:49</td>
        <td>protodog</td>
        <td>None</td>
        <td>Pure Breed</td>
        <td>Herding</td>
        <td>fd27b5ba-7144-11e5-ba71-058fbc01cf0b</td>
        <td>ce1353d8-7144-11e5-ba71-058fbc01cf0b</td>
        <td>20</td>
        <td>0.41330713937</td>
        <td>595.1622807</td>
        <td>0.0058449074865</td>
        <td>8.4166667806</td>
        <td>7.8528356481</td>
        <td>11308.083333</td>
    </tr>
    <tr>
        <td>male</td>
        <td>2012</td>
        <td>Golden Retriever</td>
        <td>70</td>
        <td>0</td>
        <td>1</td>
        <td>2013-02-05 17:22:56</td>
        <td>2013-07-25 19:41:49</td>
        <td>None</td>
        <td>None</td>
        <td>Pure Breed</td>
        <td>Sporting</td>
        <td>fd27b6b4-7144-11e5-ba71-058fbc01cf0b</td>
        <td>ce135ab8-7144-11e5-ba71-058fbc01cf0b</td>
        <td>2</td>
        <td>0.0091319445066</td>
        <td>13.15000009</td>
        <td>0.0091319445066</td>
        <td>13.15000009</td>
        <td>0.0091319445066</td>
        <td>13.15000009</td>
    </tr>
    <tr>
        <td>male</td>
        <td>2011</td>
        <td>Golden Retriever</td>
        <td>70</td>
        <td>0</td>
        <td>0</td>
        <td>2013-02-05 17:40:57</td>
        <td>2014-05-30 15:52:53</td>
        <td>None</td>
        <td>None</td>
        <td>Pure Breed</td>
        <td>Sporting</td>
        <td>fd27b79a-7144-11e5-ba71-058fbc01cf0b</td>
        <td>ce13507c-7144-11e5-ba71-058fbc01cf0b</td>
        <td>11</td>
        <td>56.115179398</td>
        <td>80805.858333</td>
        <td>0.0044328703647</td>
        <td>6.3833333252</td>
        <td>561.15179398</td>
        <td>808058.58333</td>
    </tr>
    <tr>
        <td>female</td>
        <td>2010</td>
        <td>Shih Tzu</td>
        <td>190</td>
        <td>0</td>
        <td>0</td>
        <td>2013-02-05 18:12:28</td>
        <td>2014-05-30 15:52:54</td>
        <td>einstein</td>
        <td>1</td>
        <td>Pure Breed</td>
        <td>Toy</td>
        <td>fd27b86c-7144-11e5-ba71-058fbc01cf0b</td>
        <td>ce135e14-7144-11e5-ba71-058fbc01cf0b</td>
        <td>31</td>
        <td>7.7342542438</td>
        <td>11137.326111</td>
        <td>0.00039930554425</td>
        <td>0.57499998372</td>
        <td>232.02762731</td>
        <td>334119.78333</td>
    </tr>
</table>




```python
%%sql
SELECT breed_type, AVG(mean_iti_minutes) AS avg_time, AVG(total_tests_completed) AS avg_test
FROM dogs
GROUP BY breed_type
ORDER BY avg_test DESC
;
```

    4 rows affected.





<table>
    <tr>
        <th>breed_type</th>
        <th>avg_time</th>
        <th>avg_test</th>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>2834.3205728931534</td>
        <td>10.257530120481928</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>2872.351156110182</td>
        <td>9.945900537634408</td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>3193.350493795222</td>
        <td>9.871602824737856</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>3023.0711302156274</td>
        <td>9.54250850170034</td>
    </tr>
</table>



**Question 5: Write a query that outputs the average amount of time it took customers to complete each type of test where any individual reaction times over 6000 hours are excluded and only average reaction times that are greater than 0 seconds are included (your output should end up with 67 rows).**



```python
%%sql
SELECT AVG(TIMESTAMPDIFF(minute, start_time, end_time)) AS avg
FROM exam_answers
WHERE TIMESTAMPDIFF(minute,start_time, end_time) < 6000*60 AND TIMESTAMPDIFF(minute,start_time, end_time) > 0
GROUP BY test_name
ORDER BY avg DESC;
```

    67 rows affected.





<table>
    <tr>
        <th>avg</th>
    </tr>
    <tr>
        <td>48377.4242</td>
    </tr>
    <tr>
        <td>43075.9768</td>
    </tr>
    <tr>
        <td>42991.3284</td>
    </tr>
    <tr>
        <td>32006.9579</td>
    </tr>
    <tr>
        <td>29554.7041</td>
    </tr>
    <tr>
        <td>28020.7028</td>
    </tr>
    <tr>
        <td>21292.7204</td>
    </tr>
    <tr>
        <td>20899.5196</td>
    </tr>
    <tr>
        <td>20588.9776</td>
    </tr>
    <tr>
        <td>19293.1212</td>
    </tr>
    <tr>
        <td>18849.5862</td>
    </tr>
    <tr>
        <td>16259.5040</td>
    </tr>
    <tr>
        <td>15439.6141</td>
    </tr>
    <tr>
        <td>15396.2685</td>
    </tr>
    <tr>
        <td>15015.8148</td>
    </tr>
    <tr>
        <td>12214.8392</td>
    </tr>
    <tr>
        <td>11076.5012</td>
    </tr>
    <tr>
        <td>10383.7212</td>
    </tr>
    <tr>
        <td>9960.2326</td>
    </tr>
    <tr>
        <td>9510.0490</td>
    </tr>
    <tr>
        <td>7741.1802</td>
    </tr>
    <tr>
        <td>7584.6923</td>
    </tr>
    <tr>
        <td>7022.1423</td>
    </tr>
    <tr>
        <td>6642.7766</td>
    </tr>
    <tr>
        <td>6576.4182</td>
    </tr>
    <tr>
        <td>6493.8882</td>
    </tr>
    <tr>
        <td>6468.5986</td>
    </tr>
    <tr>
        <td>6195.0640</td>
    </tr>
    <tr>
        <td>6153.3103</td>
    </tr>
    <tr>
        <td>5312.4337</td>
    </tr>
    <tr>
        <td>3523.0000</td>
    </tr>
    <tr>
        <td>3448.9583</td>
    </tr>
    <tr>
        <td>3125.1730</td>
    </tr>
    <tr>
        <td>2861.8518</td>
    </tr>
    <tr>
        <td>2711.2354</td>
    </tr>
    <tr>
        <td>2672.3636</td>
    </tr>
    <tr>
        <td>2447.6055</td>
    </tr>
    <tr>
        <td>2205.2904</td>
    </tr>
    <tr>
        <td>2168.5308</td>
    </tr>
    <tr>
        <td>1741.0616</td>
    </tr>
    <tr>
        <td>1662.8998</td>
    </tr>
    <tr>
        <td>1386.3846</td>
    </tr>
    <tr>
        <td>1018.9764</td>
    </tr>
    <tr>
        <td>959.0130</td>
    </tr>
    <tr>
        <td>887.0987</td>
    </tr>
    <tr>
        <td>868.5361</td>
    </tr>
    <tr>
        <td>387.7619</td>
    </tr>
    <tr>
        <td>313.8500</td>
    </tr>
    <tr>
        <td>240.9062</td>
    </tr>
    <tr>
        <td>216.6777</td>
    </tr>
    <tr>
        <td>206.8462</td>
    </tr>
    <tr>
        <td>164.7500</td>
    </tr>
    <tr>
        <td>133.6302</td>
    </tr>
    <tr>
        <td>125.5495</td>
    </tr>
    <tr>
        <td>87.9315</td>
    </tr>
    <tr>
        <td>79.9286</td>
    </tr>
    <tr>
        <td>78.2825</td>
    </tr>
    <tr>
        <td>76.9373</td>
    </tr>
    <tr>
        <td>48.8800</td>
    </tr>
    <tr>
        <td>43.7033</td>
    </tr>
    <tr>
        <td>4.2667</td>
    </tr>
    <tr>
        <td>2.6129</td>
    </tr>
    <tr>
        <td>1.9333</td>
    </tr>
    <tr>
        <td>1.8182</td>
    </tr>
    <tr>
        <td>1.8065</td>
    </tr>
    <tr>
        <td>1.2593</td>
    </tr>
    <tr>
        <td>1.1667</td>
    </tr>
</table>



**Question 6: Write a query that outputs the total number of unique User_Guids in each combination of State and ZIP code (postal code) in the United States, sorted first by state name in ascending alphabetical order, and second by total number of unique User_Guids in descending order (your first state should be AE and there should be 5043 rows in total in your output).**


```python
%%sql
SELECT state, zip, COUNT(DISTINCT user_guid) as uni_user
FROM users
WHERE country='US'
GROUP BY state, zip
ORDER BY state, zip desc;
```

    5043 rows affected.





<table>
    <tr>
        <th>state</th>
        <th>zip</th>
        <th>uni_user</th>
    </tr>
    <tr>
        <td>AE</td>
        <td>9845</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AE</td>
        <td>9469</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AE</td>
        <td>9128</td>
        <td>2</td>
    </tr>
    <tr>
        <td>AE</td>
        <td>9107</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AE</td>
        <td>9053</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AK</td>
        <td>99928</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AK</td>
        <td>99824</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AK</td>
        <td>99775</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AK</td>
        <td>99752</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AK</td>
        <td>99712</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AK</td>
        <td>99709</td>
        <td>3</td>
    </tr>
    <tr>
        <td>AK</td>
        <td>99705</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AK</td>
        <td>99676</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AK</td>
        <td>99645</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AK</td>
        <td>99611</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AK</td>
        <td>99587</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AK</td>
        <td>99577</td>
        <td>2</td>
    </tr>
    <tr>
        <td>AK</td>
        <td>99567</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AK</td>
        <td>99518</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AK</td>
        <td>99516</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AK</td>
        <td>99509</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AK</td>
        <td>99507</td>
        <td>3</td>
    </tr>
    <tr>
        <td>AK</td>
        <td>99502</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AK</td>
        <td>99501</td>
        <td>2</td>
    </tr>
    <tr>
        <td>AL</td>
        <td>36832</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AL</td>
        <td>36801</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AL</td>
        <td>36695</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AL</td>
        <td>36609</td>
        <td>2</td>
    </tr>
    <tr>
        <td>AL</td>
        <td>36604</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AL</td>
        <td>36602</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AL</td>
        <td>36561</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AL</td>
        <td>36532</td>
        <td>2</td>
    </tr>
    <tr>
        <td>AL</td>
        <td>36527</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AL</td>
        <td>36375</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AL</td>
        <td>36303</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AL</td>
        <td>36203</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AL</td>
        <td>36116</td>
        <td>2</td>
    </tr>
    <tr>
        <td>AL</td>
        <td>36106</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AL</td>
        <td>36104</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AL</td>
        <td>36037</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AL</td>
        <td>35976</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AL</td>
        <td>35906</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AL</td>
        <td>35803</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AL</td>
        <td>35801</td>
        <td>2</td>
    </tr>
    <tr>
        <td>AL</td>
        <td>35763</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AL</td>
        <td>35760</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AL</td>
        <td>35758</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AL</td>
        <td>35674</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AL</td>
        <td>35662</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AL</td>
        <td>35646</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AL</td>
        <td>35476</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AL</td>
        <td>35405</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AL</td>
        <td>35242</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AL</td>
        <td>35216</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AL</td>
        <td>35209</td>
        <td>4</td>
    </tr>
    <tr>
        <td>AL</td>
        <td>35205</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AL</td>
        <td>35179</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AL</td>
        <td>35121</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AL</td>
        <td>35094</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AL</td>
        <td>35007</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AL</td>
        <td>35004</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AP</td>
        <td>96377</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AP</td>
        <td>96367</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AP</td>
        <td>96310</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AP</td>
        <td>96205</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AR</td>
        <td>72956</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AR</td>
        <td>72908</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AR</td>
        <td>72901</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AR</td>
        <td>72802</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AR</td>
        <td>72762</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AR</td>
        <td>72756</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AR</td>
        <td>72714</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AR</td>
        <td>72712</td>
        <td>2</td>
    </tr>
    <tr>
        <td>AR</td>
        <td>72704</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AR</td>
        <td>72703</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AR</td>
        <td>72701</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AR</td>
        <td>72632</td>
        <td>2</td>
    </tr>
    <tr>
        <td>AR</td>
        <td>72631</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AR</td>
        <td>72554</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AR</td>
        <td>72401</td>
        <td>3</td>
    </tr>
    <tr>
        <td>AR</td>
        <td>72223</td>
        <td>2</td>
    </tr>
    <tr>
        <td>AR</td>
        <td>72212</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AR</td>
        <td>72207</td>
        <td>3</td>
    </tr>
    <tr>
        <td>AR</td>
        <td>72206</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AR</td>
        <td>72202</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AR</td>
        <td>72201</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AR</td>
        <td>72135</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AR</td>
        <td>72113</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AR</td>
        <td>72058</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AR</td>
        <td>72042</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AR</td>
        <td>72034</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AR</td>
        <td>72015</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AR</td>
        <td>71913</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AR</td>
        <td>71909</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>N/A</td>
        <td>4</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>86504</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>86426</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>86403</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>86351</td>
        <td>2</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>86336</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>86327</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>86326</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>86323</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>86314</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>86312</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>86305</td>
        <td>3</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>86303</td>
        <td>14</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>86301</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>86002</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85755</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85750</td>
        <td>4</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85749</td>
        <td>5</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85748</td>
        <td>2</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85745</td>
        <td>2</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85743</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85739</td>
        <td>2</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85737</td>
        <td>3</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85730</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85719</td>
        <td>4</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85718</td>
        <td>6</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85716</td>
        <td>4</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85715</td>
        <td>2</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85712</td>
        <td>2</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85711</td>
        <td>5</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85710</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85704</td>
        <td>2</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85658</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85650</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85646</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85641</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85636</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85635</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85622</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85615</td>
        <td>2</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85614</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85392</td>
        <td>3</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85385</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85382</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85374</td>
        <td>2</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85365</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85353</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85340</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85338</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85335</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85327</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85308</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85304</td>
        <td>2</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85303</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85296</td>
        <td>3</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85286</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85284</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85283</td>
        <td>3</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85282</td>
        <td>3</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85281</td>
        <td>2</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85268</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85266</td>
        <td>4</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85262</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85260</td>
        <td>5</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85259</td>
        <td>2</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85257</td>
        <td>3</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85255</td>
        <td>3</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85254</td>
        <td>5</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85253</td>
        <td>5</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85251</td>
        <td>2</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85250</td>
        <td>3</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85249</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85248</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85233</td>
        <td>3</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85226</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85212</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85210</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85209</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85207</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85206</td>
        <td>2</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85205</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85203</td>
        <td>2</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85202</td>
        <td>2</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85143</td>
        <td>2</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85140</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85138</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85128</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85122</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85120</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85119</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85118</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85086</td>
        <td>2</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85083</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85069</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85050</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85048</td>
        <td>3</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85045</td>
        <td>2</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85044</td>
        <td>3</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85042</td>
        <td>3</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85032</td>
        <td>3</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85029</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85028</td>
        <td>2</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85027</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85024</td>
        <td>2</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85022</td>
        <td>3</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85021</td>
        <td>3</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85020</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85016</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85015</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85013</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85012</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85008</td>
        <td>1</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85006</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>N/A</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>96161</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>96151</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>96145</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>96141</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>96107</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>96104</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>96073</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>96067</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>96022</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>96003</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>96002</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>96001</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95965</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95959</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95949</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95945</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95926</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95864</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95843</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95835</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95834</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95833</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95831</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95819</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95818</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95816</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95811</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95765</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95762</td>
        <td>6</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95747</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95746</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95722</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95695</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95694</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95692</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95691</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95688</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95682</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95678</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95677</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95650</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95648</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95633</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95630</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95628</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95624</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95621</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95620</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95618</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95616</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95610</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95608</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95605</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95603</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95602</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95570</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95540</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95536</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95519</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95503</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95501</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95492</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95482</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95476</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95472</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95470</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95465</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95460</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95457</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95448</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95442</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95437</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95436</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95425</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95409</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95407</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95405</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95404</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95403</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95401</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95383</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95366</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95361</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95356</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95355</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95354</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95236</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95227</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95212</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95138</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95136</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95134</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95132</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95128</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95125</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95124</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95123</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95120</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95119</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95116</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95113</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95112</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95110</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95076</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95070</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95065</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95062</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95060</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95051</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95050</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95046</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95037</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95033</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95032</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95030</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95023</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95020</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95018</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95014</td>
        <td>6</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95010</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95008</td>
        <td>6</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95005</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95003</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94970</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94966</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94965</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94963</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94960</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94955</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94954</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94952</td>
        <td>6</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94951</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94949</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94947</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94941</td>
        <td>9</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94939</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94930</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94928</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94925</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94920</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94904</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94903</td>
        <td>6</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94901</td>
        <td>6</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94709</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94708</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94707</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94706</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94705</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94704</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94703</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94702</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94619</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94618</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94611</td>
        <td>9</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94610</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94609</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94608</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94607</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94606</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94605</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94602</td>
        <td>7</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94599</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94598</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94597</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94596</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94595</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94591</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94590</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94588</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94585</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94583</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94582</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94580</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94577</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94574</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94571</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94568</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94566</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94565</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94564</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94563</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94560</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94559</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94558</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94556</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94555</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94553</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94551</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94550</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94549</td>
        <td>6</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94547</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94546</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94545</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94544</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94542</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94539</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94538</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94536</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94534</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94531</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94530</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94528</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94526</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94523</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94521</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94520</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94519</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94518</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94515</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94510</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94507</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94506</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94505</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94503</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94502</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94501</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94404</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94403</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94402</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94306</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94304</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94303</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94301</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94158</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94134</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94133</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94132</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94131</td>
        <td>8</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94129</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94127</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94123</td>
        <td>6</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94122</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94121</td>
        <td>7</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94118</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94117</td>
        <td>7</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94116</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94115</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94114</td>
        <td>9</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94112</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94110</td>
        <td>10</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94109</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94107</td>
        <td>12</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94103</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94102</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94089</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94087</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94086</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94080</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94070</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94063</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94062</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94061</td>
        <td>6</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94044</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94043</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94041</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94040</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94027</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94025</td>
        <td>9</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94024</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94022</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94018</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94015</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94014</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94011</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94010</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94002</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93955</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93953</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93940</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93924</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93923</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93908</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93907</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93730</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93726</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93722</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93720</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93711</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93710</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93654</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93643</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93637</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93619</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93611</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93562</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93561</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93550</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93549</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93546</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93536</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93534</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93463</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93458</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93452</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93447</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93446</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93444</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93443</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93428</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93422</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93420</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93405</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93402</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93401</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93312</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93311</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93309</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93308</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93292</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93291</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93257</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93243</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93230</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93225</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93150</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93117</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93110</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93108</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93105</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93103</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93065</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93063</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93041</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93036</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93035</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93023</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93021</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93013</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93012</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93010</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93003</td>
        <td>7</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92886</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92881</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92880</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92870</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92869</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92867</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92865</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92835</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92831</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92821</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92807</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92806</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92782</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92780</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92708</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92707</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92705</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92701</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92694</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92692</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92691</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92688</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92683</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92677</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92675</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92673</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92672</td>
        <td>6</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92663</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92660</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92657</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92656</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92653</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92651</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92649</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92648</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92647</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92646</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92637</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92629</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92627</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92626</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92625</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92620</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92618</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92612</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92610</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92606</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92603</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92602</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92595</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92593</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92592</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92590</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92586</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92562</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92549</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92545</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92516</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92506</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92504</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92503</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92374</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92373</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92320</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92307</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92270</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92263</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92262</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92260</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92253</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92247</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92232</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92223</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92211</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92163</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92143</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92131</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92130</td>
        <td>12</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92129</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92128</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92127</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92126</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92124</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92123</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92122</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92120</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92119</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92118</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92117</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92116</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92115</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92111</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92110</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92109</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92107</td>
        <td>16</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92106</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92105</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92104</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92103</td>
        <td>6</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92102</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92101</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92092</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92091</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92084</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92081</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92078</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92075</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92072</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92071</td>
        <td>6</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92067</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92065</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92064</td>
        <td>8</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92059</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92058</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92057</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92056</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92054</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92046</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92040</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92038</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92037</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92028</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92027</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92026</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92025</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92024</td>
        <td>10</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92021</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92020</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92019</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92014</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92011</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92010</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92009</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92008</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92007</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92003</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91945</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91942</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91941</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91931</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91921</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91913</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91910</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91908</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91902</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91901</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91801</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91791</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91789</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91786</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91776</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91775</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91770</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91764</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91755</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91750</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91748</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91737</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91730</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91723</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91711</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91702</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91701</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91607</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91606</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91604</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91602</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91505</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91502</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91501</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91436</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91423</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91411</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91406</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91405</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91403</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91387</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91377</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91367</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91364</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91361</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91356</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91355</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91354</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91335</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91326</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91325</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91324</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91321</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91320</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91316</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91311</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91307</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91303</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91302</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91301</td>
        <td>6</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91214</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91208</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91207</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91205</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91204</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91203</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91201</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91106</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91105</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91104</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91101</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91042</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91041</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91030</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91016</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91011</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91006</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91001</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90815</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90814</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90813</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90810</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90808</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90807</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90806</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90804</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90803</td>
        <td>7</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90755</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90740</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90731</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90720</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90704</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90638</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90504</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90503</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90405</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90404</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90403</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90402</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90401</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90293</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90292</td>
        <td>7</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90291</td>
        <td>7</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90290</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90278</td>
        <td>7</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90277</td>
        <td>6</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90274</td>
        <td>6</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90272</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90266</td>
        <td>7</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90265</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90247</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90242</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90232</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90230</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90212</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90211</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90210</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90077</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90071</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90069</td>
        <td>8</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90068</td>
        <td>8</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90067</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90066</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90065</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90064</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90051</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90049</td>
        <td>8</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90048</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90046</td>
        <td>13</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90045</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90043</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90042</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90041</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90039</td>
        <td>6</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90036</td>
        <td>6</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90034</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90031</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90029</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90027</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90026</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90025</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90024</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90020</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90019</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90017</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90016</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90015</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90014</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90012</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90005</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90004</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>81652</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>81639</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>81625</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>81623</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>81621</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>81620</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>81611</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>81601</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>81507</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>81501</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>81403</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>81301</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>81252</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>81236</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>81235</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>81201</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>81131</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>81007</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80962</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80923</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80922</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80919</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80918</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80917</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80911</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80908</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80906</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80904</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80864</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80829</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80827</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80813</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80808</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80644</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80643</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80634</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80631</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80602</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80547</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80542</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80540</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80537</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80534</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80528</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80527</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80526</td>
        <td>7</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80525</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80524</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80521</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80517</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80516</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80504</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80503</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80501</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80498</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80488</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80487</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80466</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80465</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80439</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80430</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80422</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80403</td>
        <td>6</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80401</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80308</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80304</td>
        <td>10</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80303</td>
        <td>7</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80302</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80301</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80247</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80238</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80237</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80234</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80233</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80230</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80228</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80227</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80226</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80223</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80222</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80220</td>
        <td>6</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80218</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80216</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80215</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80214</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80212</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80211</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80210</td>
        <td>9</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80209</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80207</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80206</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80205</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80204</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80203</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80202</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80138</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80134</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80132</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80129</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80128</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80127</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80126</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80124</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80123</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80122</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80121</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80120</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80116</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80113</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80112</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80111</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80109</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80108</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80107</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80106</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80104</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80033</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80031</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80027</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80026</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80023</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80022</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80021</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80020</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80016</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80015</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80014</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80013</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80012</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80011</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80010</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80005</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80004</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80002</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80000</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CT</td>
        <td>N/A</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CT</td>
        <td>6907</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CT</td>
        <td>6905</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CT</td>
        <td>6903</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CT</td>
        <td>6902</td>
        <td>4</td>
    </tr>
    <tr>
        <td>CT</td>
        <td>6897</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CT</td>
        <td>6896</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CT</td>
        <td>6890</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CT</td>
        <td>6883</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CT</td>
        <td>6880</td>
        <td>8</td>
    </tr>
    <tr>
        <td>CT</td>
        <td>6878</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CT</td>
        <td>6877</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CT</td>
        <td>6870</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CT</td>
        <td>6854</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CT</td>
        <td>6853</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CT</td>
        <td>6851</td>
        <td>3</td>
    </tr>
    <tr>
        <td>CT</td>
        <td>6840</td>
        <td>6</td>
    </tr>
    <tr>
        <td>CT</td>
        <td>6831</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CT</td>
        <td>6830</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CT</td>
        <td>6824</td>
        <td>6</td>
    </tr>
    <tr>
        <td>CT</td>
        <td>6820</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CT</td>
        <td>6811</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CT</td>
        <td>6810</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CT</td>
        <td>6801</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CT</td>
        <td>6798</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CT</td>
        <td>6795</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CT</td>
        <td>6777</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CT</td>
        <td>6776</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CT</td>
        <td>6762</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CT</td>
        <td>6759</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CT</td>
        <td>6756</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CT</td>
        <td>6752</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CT</td>
        <td>6614</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CT</td>
        <td>6612</td>
        <td>2</td>
    </tr>
    <tr>
        <td>CT</td>
        <td>6611</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CT</td>
        <td>6606</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CT</td>
        <td>6519</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CT</td>
        <td>6518</td>
        <td>1</td>
    </tr>
    <tr>
        <td>CT</td>
        <td>6517</td>
        <td>3</td>
    </tr>
</table>
<span style="font-style:italic;text-align:center;">5043 rows, truncated to displaylimit of 1000</span>




```python
%%sql
select *
from users
limit 1;
```

    1 rows affected.





<table>
    <tr>
        <th>sign_in_count</th>
        <th>created_at</th>
        <th>updated_at</th>
        <th>max_dogs</th>
        <th>membership_id</th>
        <th>subscribed</th>
        <th>exclude</th>
        <th>free_start_user</th>
        <th>last_active_at</th>
        <th>membership_type</th>
        <th>user_guid</th>
        <th>city</th>
        <th>state</th>
        <th>zip</th>
        <th>country</th>
        <th>utc_correction</th>
    </tr>
    <tr>
        <td>14</td>
        <td>2013-02-05 03:52:02</td>
        <td>2015-03-12 00:25:15</td>
        <td>2</td>
        <td>2</td>
        <td>1</td>
        <td>None</td>
        <td>None</td>
        <td>2015-03-12 00:25:15</td>
        <td>2</td>
        <td>ce134e42-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Grand Forks</td>
        <td>ND</td>
        <td>58201</td>
        <td>US</td>
        <td>-6</td>
    </tr>
</table>



**Question 7: Write a query that outputs the total number of unique User_Guids in each combination of State and ZIP code in the United States *that have at least 5 users*, sorted first by state name in ascending alphabetical order, and second by total number of unique User_Guids in descending order (your first state/ZIP code combination should be AZ/86303).**


```python
%%sql
SELECT state, zip, COUNT(DISTINCT user_guid) as uni_user
FROM users
WHERE country='US'
GROUP BY state, zip
HAVING uni_user > 4
ORDER BY state, zip desc;
```

    285 rows affected.





<table>
    <tr>
        <th>state</th>
        <th>zip</th>
        <th>uni_user</th>
    </tr>
    <tr>
        <td>AZ</td>
        <td>86303</td>
        <td>14</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85749</td>
        <td>5</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85718</td>
        <td>6</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85711</td>
        <td>5</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85260</td>
        <td>5</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85254</td>
        <td>5</td>
    </tr>
    <tr>
        <td>AZ</td>
        <td>85253</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95818</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95762</td>
        <td>6</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95476</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95014</td>
        <td>6</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95008</td>
        <td>6</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>95003</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94952</td>
        <td>6</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94941</td>
        <td>9</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94904</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94903</td>
        <td>6</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94901</td>
        <td>6</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94706</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94611</td>
        <td>9</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94602</td>
        <td>7</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94597</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94550</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94549</td>
        <td>6</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94510</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94131</td>
        <td>8</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94123</td>
        <td>6</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94121</td>
        <td>7</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94118</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94117</td>
        <td>7</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94114</td>
        <td>9</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94110</td>
        <td>10</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94109</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94107</td>
        <td>12</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94061</td>
        <td>6</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94040</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>94025</td>
        <td>9</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93940</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93105</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93023</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93012</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>93003</td>
        <td>7</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92672</td>
        <td>6</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92211</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92130</td>
        <td>12</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92122</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92107</td>
        <td>16</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92106</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92103</td>
        <td>6</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92101</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92071</td>
        <td>6</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92064</td>
        <td>8</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92024</td>
        <td>10</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>92009</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91406</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>91301</td>
        <td>6</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90803</td>
        <td>7</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90405</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90292</td>
        <td>7</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90291</td>
        <td>7</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90278</td>
        <td>7</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90277</td>
        <td>6</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90274</td>
        <td>6</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90266</td>
        <td>7</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90232</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90210</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90069</td>
        <td>8</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90068</td>
        <td>8</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90049</td>
        <td>8</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90046</td>
        <td>13</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90039</td>
        <td>6</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90036</td>
        <td>6</td>
    </tr>
    <tr>
        <td>CA</td>
        <td>90025</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80526</td>
        <td>7</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80403</td>
        <td>6</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80401</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80304</td>
        <td>10</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80303</td>
        <td>7</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80227</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80220</td>
        <td>6</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80210</td>
        <td>9</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80206</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80205</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CO</td>
        <td>80126</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CT</td>
        <td>6880</td>
        <td>8</td>
    </tr>
    <tr>
        <td>CT</td>
        <td>6840</td>
        <td>6</td>
    </tr>
    <tr>
        <td>CT</td>
        <td>6824</td>
        <td>6</td>
    </tr>
    <tr>
        <td>CT</td>
        <td>6820</td>
        <td>5</td>
    </tr>
    <tr>
        <td>CT</td>
        <td>6614</td>
        <td>5</td>
    </tr>
    <tr>
        <td>DC</td>
        <td>20016</td>
        <td>7</td>
    </tr>
    <tr>
        <td>DC</td>
        <td>20011</td>
        <td>6</td>
    </tr>
    <tr>
        <td>DC</td>
        <td>20009</td>
        <td>14</td>
    </tr>
    <tr>
        <td>DC</td>
        <td>20007</td>
        <td>8</td>
    </tr>
    <tr>
        <td>DC</td>
        <td>20005</td>
        <td>6</td>
    </tr>
    <tr>
        <td>DC</td>
        <td>20003</td>
        <td>5</td>
    </tr>
    <tr>
        <td>DC</td>
        <td>20002</td>
        <td>8</td>
    </tr>
    <tr>
        <td>DC</td>
        <td>20001</td>
        <td>7</td>
    </tr>
    <tr>
        <td>DE</td>
        <td>19958</td>
        <td>7</td>
    </tr>
    <tr>
        <td>FL</td>
        <td>33647</td>
        <td>6</td>
    </tr>
    <tr>
        <td>FL</td>
        <td>33418</td>
        <td>6</td>
    </tr>
    <tr>
        <td>FL</td>
        <td>33156</td>
        <td>5</td>
    </tr>
    <tr>
        <td>FL</td>
        <td>32765</td>
        <td>5</td>
    </tr>
    <tr>
        <td>FL</td>
        <td>32751</td>
        <td>5</td>
    </tr>
    <tr>
        <td>FL</td>
        <td>32312</td>
        <td>6</td>
    </tr>
    <tr>
        <td>GA</td>
        <td>30345</td>
        <td>6</td>
    </tr>
    <tr>
        <td>GA</td>
        <td>30328</td>
        <td>5</td>
    </tr>
    <tr>
        <td>GA</td>
        <td>30316</td>
        <td>5</td>
    </tr>
    <tr>
        <td>GA</td>
        <td>30308</td>
        <td>5</td>
    </tr>
    <tr>
        <td>GA</td>
        <td>30305</td>
        <td>7</td>
    </tr>
    <tr>
        <td>GA</td>
        <td>30067</td>
        <td>5</td>
    </tr>
    <tr>
        <td>GA</td>
        <td>30004</td>
        <td>7</td>
    </tr>
    <tr>
        <td>HI</td>
        <td>96734</td>
        <td>8</td>
    </tr>
    <tr>
        <td>ID</td>
        <td>83702</td>
        <td>9</td>
    </tr>
    <tr>
        <td>IL</td>
        <td>60660</td>
        <td>7</td>
    </tr>
    <tr>
        <td>IL</td>
        <td>60657</td>
        <td>9</td>
    </tr>
    <tr>
        <td>IL</td>
        <td>60654</td>
        <td>11</td>
    </tr>
    <tr>
        <td>IL</td>
        <td>60647</td>
        <td>6</td>
    </tr>
    <tr>
        <td>IL</td>
        <td>60642</td>
        <td>5</td>
    </tr>
    <tr>
        <td>IL</td>
        <td>60640</td>
        <td>9</td>
    </tr>
    <tr>
        <td>IL</td>
        <td>60626</td>
        <td>5</td>
    </tr>
    <tr>
        <td>IL</td>
        <td>60618</td>
        <td>6</td>
    </tr>
    <tr>
        <td>IL</td>
        <td>60614</td>
        <td>18</td>
    </tr>
    <tr>
        <td>IL</td>
        <td>60613</td>
        <td>8</td>
    </tr>
    <tr>
        <td>IL</td>
        <td>60610</td>
        <td>7</td>
    </tr>
    <tr>
        <td>IL</td>
        <td>60093</td>
        <td>5</td>
    </tr>
    <tr>
        <td>IN</td>
        <td>47401</td>
        <td>6</td>
    </tr>
    <tr>
        <td>KS</td>
        <td>66062</td>
        <td>6</td>
    </tr>
    <tr>
        <td>LA</td>
        <td>70118</td>
        <td>6</td>
    </tr>
    <tr>
        <td>LA</td>
        <td>70115</td>
        <td>8</td>
    </tr>
    <tr>
        <td>MA</td>
        <td>2472</td>
        <td>5</td>
    </tr>
    <tr>
        <td>MA</td>
        <td>2143</td>
        <td>5</td>
    </tr>
    <tr>
        <td>MA</td>
        <td>2135</td>
        <td>5</td>
    </tr>
    <tr>
        <td>MA</td>
        <td>2130</td>
        <td>5</td>
    </tr>
    <tr>
        <td>MA</td>
        <td>2129</td>
        <td>6</td>
    </tr>
    <tr>
        <td>MA</td>
        <td>2127</td>
        <td>8</td>
    </tr>
    <tr>
        <td>MA</td>
        <td>2116</td>
        <td>5</td>
    </tr>
    <tr>
        <td>MD</td>
        <td>21286</td>
        <td>6</td>
    </tr>
    <tr>
        <td>MD</td>
        <td>21230</td>
        <td>5</td>
    </tr>
    <tr>
        <td>MD</td>
        <td>21228</td>
        <td>5</td>
    </tr>
    <tr>
        <td>MD</td>
        <td>20910</td>
        <td>7</td>
    </tr>
    <tr>
        <td>MD</td>
        <td>20895</td>
        <td>5</td>
    </tr>
    <tr>
        <td>MD</td>
        <td>20878</td>
        <td>6</td>
    </tr>
    <tr>
        <td>MD</td>
        <td>20854</td>
        <td>8</td>
    </tr>
    <tr>
        <td>MD</td>
        <td>20852</td>
        <td>5</td>
    </tr>
    <tr>
        <td>MD</td>
        <td>20817</td>
        <td>7</td>
    </tr>
    <tr>
        <td>MI</td>
        <td>48103</td>
        <td>8</td>
    </tr>
    <tr>
        <td>MN</td>
        <td>55426</td>
        <td>6</td>
    </tr>
    <tr>
        <td>MO</td>
        <td>63139</td>
        <td>6</td>
    </tr>
    <tr>
        <td>MO</td>
        <td>63122</td>
        <td>5</td>
    </tr>
    <tr>
        <td>MT</td>
        <td>59715</td>
        <td>5</td>
    </tr>
    <tr>
        <td>N/A</td>
        <td>N/A</td>
        <td>83</td>
    </tr>
    <tr>
        <td>NC</td>
        <td>28787</td>
        <td>6</td>
    </tr>
    <tr>
        <td>NC</td>
        <td>28374</td>
        <td>6</td>
    </tr>
    <tr>
        <td>NC</td>
        <td>28270</td>
        <td>6</td>
    </tr>
    <tr>
        <td>NC</td>
        <td>28226</td>
        <td>5</td>
    </tr>
    <tr>
        <td>NC</td>
        <td>28205</td>
        <td>5</td>
    </tr>
    <tr>
        <td>NC</td>
        <td>27713</td>
        <td>10</td>
    </tr>
    <tr>
        <td>NC</td>
        <td>27707</td>
        <td>17</td>
    </tr>
    <tr>
        <td>NC</td>
        <td>27705</td>
        <td>26</td>
    </tr>
    <tr>
        <td>NC</td>
        <td>27701</td>
        <td>32</td>
    </tr>
    <tr>
        <td>NC</td>
        <td>27617</td>
        <td>9</td>
    </tr>
    <tr>
        <td>NC</td>
        <td>27615</td>
        <td>11</td>
    </tr>
    <tr>
        <td>NC</td>
        <td>27614</td>
        <td>7</td>
    </tr>
    <tr>
        <td>NC</td>
        <td>27613</td>
        <td>11</td>
    </tr>
    <tr>
        <td>NC</td>
        <td>27612</td>
        <td>6</td>
    </tr>
    <tr>
        <td>NC</td>
        <td>27609</td>
        <td>7</td>
    </tr>
    <tr>
        <td>NC</td>
        <td>27608</td>
        <td>7</td>
    </tr>
    <tr>
        <td>NC</td>
        <td>27607</td>
        <td>6</td>
    </tr>
    <tr>
        <td>NC</td>
        <td>27606</td>
        <td>5</td>
    </tr>
    <tr>
        <td>NC</td>
        <td>27603</td>
        <td>6</td>
    </tr>
    <tr>
        <td>NC</td>
        <td>27587</td>
        <td>6</td>
    </tr>
    <tr>
        <td>NC</td>
        <td>27539</td>
        <td>9</td>
    </tr>
    <tr>
        <td>NC</td>
        <td>27519</td>
        <td>7</td>
    </tr>
    <tr>
        <td>NC</td>
        <td>27517</td>
        <td>11</td>
    </tr>
    <tr>
        <td>NC</td>
        <td>27516</td>
        <td>17</td>
    </tr>
    <tr>
        <td>NC</td>
        <td>27514</td>
        <td>9</td>
    </tr>
    <tr>
        <td>NC</td>
        <td>27513</td>
        <td>7</td>
    </tr>
    <tr>
        <td>NC</td>
        <td>27502</td>
        <td>5</td>
    </tr>
    <tr>
        <td>NC</td>
        <td>27410</td>
        <td>6</td>
    </tr>
    <tr>
        <td>NC</td>
        <td>27278</td>
        <td>9</td>
    </tr>
    <tr>
        <td>NC</td>
        <td>27104</td>
        <td>6</td>
    </tr>
    <tr>
        <td>NJ</td>
        <td>8540</td>
        <td>5</td>
    </tr>
    <tr>
        <td>NJ</td>
        <td>7302</td>
        <td>7</td>
    </tr>
    <tr>
        <td>NJ</td>
        <td>7030</td>
        <td>8</td>
    </tr>
    <tr>
        <td>NM</td>
        <td>87111</td>
        <td>6</td>
    </tr>
    <tr>
        <td>NV</td>
        <td>89511</td>
        <td>5</td>
    </tr>
    <tr>
        <td>NY</td>
        <td>14850</td>
        <td>8</td>
    </tr>
    <tr>
        <td>NY</td>
        <td>11249</td>
        <td>7</td>
    </tr>
    <tr>
        <td>NY</td>
        <td>11238</td>
        <td>8</td>
    </tr>
    <tr>
        <td>NY</td>
        <td>11222</td>
        <td>5</td>
    </tr>
    <tr>
        <td>NY</td>
        <td>11217</td>
        <td>6</td>
    </tr>
    <tr>
        <td>NY</td>
        <td>11215</td>
        <td>5</td>
    </tr>
    <tr>
        <td>NY</td>
        <td>11211</td>
        <td>5</td>
    </tr>
    <tr>
        <td>NY</td>
        <td>11209</td>
        <td>5</td>
    </tr>
    <tr>
        <td>NY</td>
        <td>11201</td>
        <td>12</td>
    </tr>
    <tr>
        <td>NY</td>
        <td>11105</td>
        <td>5</td>
    </tr>
    <tr>
        <td>NY</td>
        <td>10708</td>
        <td>5</td>
    </tr>
    <tr>
        <td>NY</td>
        <td>10583</td>
        <td>6</td>
    </tr>
    <tr>
        <td>NY</td>
        <td>10128</td>
        <td>6</td>
    </tr>
    <tr>
        <td>NY</td>
        <td>10075</td>
        <td>5</td>
    </tr>
    <tr>
        <td>NY</td>
        <td>10028</td>
        <td>11</td>
    </tr>
    <tr>
        <td>NY</td>
        <td>10025</td>
        <td>12</td>
    </tr>
    <tr>
        <td>NY</td>
        <td>10024</td>
        <td>13</td>
    </tr>
    <tr>
        <td>NY</td>
        <td>10023</td>
        <td>13</td>
    </tr>
    <tr>
        <td>NY</td>
        <td>10022</td>
        <td>5</td>
    </tr>
    <tr>
        <td>NY</td>
        <td>10021</td>
        <td>8</td>
    </tr>
    <tr>
        <td>NY</td>
        <td>10019</td>
        <td>9</td>
    </tr>
    <tr>
        <td>NY</td>
        <td>10016</td>
        <td>10</td>
    </tr>
    <tr>
        <td>NY</td>
        <td>10014</td>
        <td>8</td>
    </tr>
    <tr>
        <td>NY</td>
        <td>10013</td>
        <td>6</td>
    </tr>
    <tr>
        <td>NY</td>
        <td>10012</td>
        <td>6</td>
    </tr>
    <tr>
        <td>NY</td>
        <td>10011</td>
        <td>9</td>
    </tr>
    <tr>
        <td>NY</td>
        <td>10003</td>
        <td>14</td>
    </tr>
    <tr>
        <td>OH</td>
        <td>45243</td>
        <td>5</td>
    </tr>
    <tr>
        <td>OH</td>
        <td>45040</td>
        <td>5</td>
    </tr>
    <tr>
        <td>OH</td>
        <td>44149</td>
        <td>5</td>
    </tr>
    <tr>
        <td>OH</td>
        <td>43235</td>
        <td>5</td>
    </tr>
    <tr>
        <td>OH</td>
        <td>43214</td>
        <td>8</td>
    </tr>
    <tr>
        <td>OH</td>
        <td>43068</td>
        <td>5</td>
    </tr>
    <tr>
        <td>OK</td>
        <td>73013</td>
        <td>5</td>
    </tr>
    <tr>
        <td>OR</td>
        <td>97702</td>
        <td>5</td>
    </tr>
    <tr>
        <td>OR</td>
        <td>97405</td>
        <td>5</td>
    </tr>
    <tr>
        <td>OR</td>
        <td>97229</td>
        <td>8</td>
    </tr>
    <tr>
        <td>OR</td>
        <td>97215</td>
        <td>5</td>
    </tr>
    <tr>
        <td>OR</td>
        <td>97212</td>
        <td>7</td>
    </tr>
    <tr>
        <td>OR</td>
        <td>97206</td>
        <td>5</td>
    </tr>
    <tr>
        <td>PA</td>
        <td>19460</td>
        <td>6</td>
    </tr>
    <tr>
        <td>PA</td>
        <td>19147</td>
        <td>6</td>
    </tr>
    <tr>
        <td>PA</td>
        <td>19087</td>
        <td>6</td>
    </tr>
    <tr>
        <td>PA</td>
        <td>15237</td>
        <td>5</td>
    </tr>
    <tr>
        <td>PA</td>
        <td>15101</td>
        <td>5</td>
    </tr>
    <tr>
        <td>SC</td>
        <td>29707</td>
        <td>5</td>
    </tr>
    <tr>
        <td>SC</td>
        <td>29464</td>
        <td>13</td>
    </tr>
    <tr>
        <td>SC</td>
        <td>29407</td>
        <td>5</td>
    </tr>
    <tr>
        <td>SC</td>
        <td>29303</td>
        <td>14</td>
    </tr>
    <tr>
        <td>SC</td>
        <td>29205</td>
        <td>5</td>
    </tr>
    <tr>
        <td>TN</td>
        <td>37205</td>
        <td>7</td>
    </tr>
    <tr>
        <td>TN</td>
        <td>37067</td>
        <td>6</td>
    </tr>
    <tr>
        <td>TN</td>
        <td>37027</td>
        <td>6</td>
    </tr>
    <tr>
        <td>TX</td>
        <td>78757</td>
        <td>6</td>
    </tr>
    <tr>
        <td>TX</td>
        <td>78750</td>
        <td>8</td>
    </tr>
    <tr>
        <td>TX</td>
        <td>78748</td>
        <td>5</td>
    </tr>
    <tr>
        <td>TX</td>
        <td>78745</td>
        <td>8</td>
    </tr>
    <tr>
        <td>TX</td>
        <td>78704</td>
        <td>6</td>
    </tr>
    <tr>
        <td>TX</td>
        <td>78703</td>
        <td>7</td>
    </tr>
    <tr>
        <td>TX</td>
        <td>78613</td>
        <td>5</td>
    </tr>
    <tr>
        <td>TX</td>
        <td>77584</td>
        <td>6</td>
    </tr>
    <tr>
        <td>TX</td>
        <td>77382</td>
        <td>5</td>
    </tr>
    <tr>
        <td>TX</td>
        <td>77381</td>
        <td>5</td>
    </tr>
    <tr>
        <td>TX</td>
        <td>77008</td>
        <td>8</td>
    </tr>
    <tr>
        <td>TX</td>
        <td>77007</td>
        <td>7</td>
    </tr>
    <tr>
        <td>TX</td>
        <td>77006</td>
        <td>5</td>
    </tr>
    <tr>
        <td>TX</td>
        <td>76712</td>
        <td>5</td>
    </tr>
    <tr>
        <td>TX</td>
        <td>75248</td>
        <td>5</td>
    </tr>
    <tr>
        <td>TX</td>
        <td>75219</td>
        <td>5</td>
    </tr>
    <tr>
        <td>TX</td>
        <td>75025</td>
        <td>5</td>
    </tr>
    <tr>
        <td>TX</td>
        <td>75023</td>
        <td>5</td>
    </tr>
    <tr>
        <td>UT</td>
        <td>84098</td>
        <td>6</td>
    </tr>
    <tr>
        <td>VA</td>
        <td>23462</td>
        <td>5</td>
    </tr>
    <tr>
        <td>VA</td>
        <td>22903</td>
        <td>7</td>
    </tr>
    <tr>
        <td>VA</td>
        <td>22902</td>
        <td>5</td>
    </tr>
    <tr>
        <td>VA</td>
        <td>22314</td>
        <td>8</td>
    </tr>
    <tr>
        <td>VA</td>
        <td>22304</td>
        <td>6</td>
    </tr>
    <tr>
        <td>VA</td>
        <td>22301</td>
        <td>5</td>
    </tr>
    <tr>
        <td>VA</td>
        <td>22201</td>
        <td>9</td>
    </tr>
    <tr>
        <td>VA</td>
        <td>22101</td>
        <td>6</td>
    </tr>
    <tr>
        <td>VA</td>
        <td>22043</td>
        <td>7</td>
    </tr>
    <tr>
        <td>VA</td>
        <td>20191</td>
        <td>9</td>
    </tr>
    <tr>
        <td>VA</td>
        <td>20147</td>
        <td>7</td>
    </tr>
    <tr>
        <td>VA</td>
        <td>20120</td>
        <td>6</td>
    </tr>
    <tr>
        <td>WA</td>
        <td>98225</td>
        <td>7</td>
    </tr>
    <tr>
        <td>WA</td>
        <td>98199</td>
        <td>6</td>
    </tr>
    <tr>
        <td>WA</td>
        <td>98122</td>
        <td>7</td>
    </tr>
    <tr>
        <td>WA</td>
        <td>98118</td>
        <td>7</td>
    </tr>
    <tr>
        <td>WA</td>
        <td>98115</td>
        <td>6</td>
    </tr>
    <tr>
        <td>WA</td>
        <td>98110</td>
        <td>5</td>
    </tr>
    <tr>
        <td>WA</td>
        <td>98106</td>
        <td>5</td>
    </tr>
    <tr>
        <td>WA</td>
        <td>98103</td>
        <td>9</td>
    </tr>
    <tr>
        <td>WA</td>
        <td>98102</td>
        <td>7</td>
    </tr>
    <tr>
        <td>WA</td>
        <td>98074</td>
        <td>6</td>
    </tr>
    <tr>
        <td>WA</td>
        <td>98072</td>
        <td>5</td>
    </tr>
    <tr>
        <td>WA</td>
        <td>98052</td>
        <td>6</td>
    </tr>
    <tr>
        <td>WA</td>
        <td>98045</td>
        <td>6</td>
    </tr>
    <tr>
        <td>WA</td>
        <td>98033</td>
        <td>6</td>
    </tr>
    <tr>
        <td>WI</td>
        <td>53213</td>
        <td>5</td>
    </tr>
</table>



<mark>**Be sure to watch the next video before beginning Exercise 6, the next set of MySQL exercises</mark>,** **and feel free to practice any other queries you wish below!**


```python

```
