
# coding: utf-8

# # JoBimText: Creating Distributional Thesaurus
# **PART 2 :** Similarity measures, Pruning, Aggregation and Sorting

# ### Import required libraries

# In[1]:


import sqlite3


# ### Open Database `thesaurus.db`

# In[2]:


conn = sqlite3.connect('thesaurus.db')
c = conn.cursor()


# ### Create table with LE-CF and corresponding Similarity measure
# We 'll use PMI here

# In[3]:


c.execute("DROP TABLE IF EXISTS sm;")

# This table's has ids corresponding to lecf's
c.execute('''CREATE TABLE sm
            (id INTEGER PRIMARY KEY,
            pmi FLOAT NOT NULL)''')

conn.commit()


# ### Calculating PMI from tables LE, CF and LE-CF
# * `pmi = le-cf.count/(le.count * cf.count)`
# * For each row of LE-CF table, compute `PMI` and insert it into `sm`

# In[4]:


c.execute('''
INSERT INTO sm (pmi, id)
SELECT pmi, id FROM
(SELECT lecfc * 1.0/(lec*cfc) as pmi,
lecfid as id from
    (SELECT lecf.id, 
            lecf.le as leid, 
            lecf.cf as cfid, 
            le.count as lec,
            le.name as lename,
            cf.count as cfc,
            lecf.count as lecfc,
            lecf.id as lecfid
        from lecf, le, cf
        where leid == le.id and cfid == cf.id)
        )''')
conn.commit()


# ### The next step is Pruning
# * Remove from `sm` values with `PMI` less than some limit
# * Since the corpus is very small, we'll also set the pruning limit to be very small
# * `pruning limit = 1.0/32768`

# ### Create Pruned Similarity Measure `psm` Table:

# In[48]:


c.execute("drop table if exists psm")
c.execute("drop table if exists simcount")

c.execute('''
CREATE TABLE psm (
id INTEGER PRIMARY KEY NOT NULL,
pmi FLOAT NOT NULL
)''')

c.execute('''
INSERT INTO psm (pmi, id)
SELECT pmi, id from sm where pmi > 1.0/(1024)
''')

c.execute('''
CREATE TABLE simcount (
le1 INTEGER NOT NULL,
le2 INTEGER NOT NULL,
count INT NOT NULL
)''')

conn.commit()


# In[49]:


c.execute('''
INSERT INTO simcount (le1, le2, count)
SELECT E.id, F.id, count(*) FROM
(SELECT A.id, B.id, 
        C.le as le1, C.cf as cf, C.id,
        D.le as le2, D.cf, D.id
    FROM psm AS A, 
         psm AS B,
         lecf AS C,
         lecf AS D
    WHERE A.id == C.id AND
          B.id == D.id AND
          C.cf == D.cf AND
          C.le <> D.le) AS sim, le AS E, le AS F 
                          where SIM.le1 == E.id AND
                                SIM.le2 == F.id
                            GROUP BY E.name, F.name
''')
conn.commit()


# ### Querying the thesaurus:

# In[61]:


def query_Thesaurus(word):
    for i in c.execute('''
    select a.name, b.name, c.count from 
    simcount as c, le as a, le as b 
    where a.id == c.le1 and 
            b.id == c.le2 and 
            c.count > 2 and 
            a.name == '{}' order by c.count desc;'''.format(word)).fetchall():
        print(i)


# ## Some intresting Results:

# In[62]:


query_Thesaurus("many")


# In[63]:


query_Thesaurus("livestock")


# In[64]:


query_Thesaurus("several")


# In[65]:


query_Thesaurus("mm")


# In[66]:


query_Thesaurus("four")

