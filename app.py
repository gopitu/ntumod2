#!/usr/bin/env python
# coding: utf-8

# In[52]:


from flask import Flask, request, render_template


# In[53]:


app = Flask(__name__)


# In[54]:


import joblib

@app.route("/", methods=["GET","POST"])
def index():
  if request.method=="POST":
    rates = request.form.get("rates")
    print(rates)
    model = joblib.load("DBS_Reg")
    pred = model.predict([[float(rates)]])
    s = "The predicted DBS Stock Price is" + str(pred)
    return(render_template("index.html", results=s))
  else:
    return(render_template("index.html", results="Loaded"))


# In[ ]:

if __name__ == "__main__":
  app.run()


# In[ ]:




