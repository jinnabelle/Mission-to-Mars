{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "69cb3b5f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[WDM] - ====== WebDriver manager ======\n",
      "INFO:WDM:====== WebDriver manager ======\n",
      "[WDM] - Current google-chrome version is 102.0.5005\n",
      "INFO:WDM:Current google-chrome version is 102.0.5005\n",
      "[WDM] - Get LATEST chromedriver version for 102.0.5005 google-chrome\n",
      "INFO:WDM:Get LATEST chromedriver version for 102.0.5005 google-chrome\n",
      "[WDM] - Driver [C:\\Users\\jinna\\.wdm\\drivers\\chromedriver\\win32\\102.0.5005.61\\chromedriver.exe] found in cache\n",
      "INFO:WDM:Driver [C:\\Users\\jinna\\.wdm\\drivers\\chromedriver\\win32\\102.0.5005.61\\chromedriver.exe] found in cache\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, render_template, redirect, url_for\n",
    "from flask_pymongo import PyMongo\n",
    "import scraping"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "457cddca",
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "108f3300",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use flask_pymongo to set up mongo connection\n",
    "app.config[\"MONGO_URI\"] = \"mongodb://localhost:27017/mars_app\"\n",
    "mongo = PyMongo(app)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "37e6d063",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/\")\n",
    "def index():\n",
    "   mars = mongo.db.mars.find_one()\n",
    "   return render_template(\"index.html\", mars=mars)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "92fbec0f",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/scrape\")\n",
    "def scrape():\n",
    "   mars = mongo.db.mars\n",
    "   mars_data = scraping.scrape_all()\n",
    "   mars.update_one({}, {\"$set\":mars_data}, upsert=True)\n",
    "   return redirect('/', code=302)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "6bc6cc3b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
      "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "INFO:werkzeug: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n",
      "ERROR:__main__:Exception on / [GET]\n",
      "Traceback (most recent call last):\n",
      "  File \"C:\\Users\\jinna\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\app.py\", line 2447, in wsgi_app\n",
      "    response = self.full_dispatch_request()\n",
      "  File \"C:\\Users\\jinna\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\app.py\", line 1952, in full_dispatch_request\n",
      "    rv = self.handle_user_exception(e)\n",
      "  File \"C:\\Users\\jinna\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\app.py\", line 1821, in handle_user_exception\n",
      "    reraise(exc_type, exc_value, tb)\n",
      "  File \"C:\\Users\\jinna\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\_compat.py\", line 39, in reraise\n",
      "    raise value\n",
      "  File \"C:\\Users\\jinna\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\app.py\", line 1950, in full_dispatch_request\n",
      "    rv = self.dispatch_request()\n",
      "  File \"C:\\Users\\jinna\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\app.py\", line 1936, in dispatch_request\n",
      "    return self.view_functions[rule.endpoint](**req.view_args)\n",
      "  File \"C:\\Users\\jinna\\AppData\\Local\\Temp/ipykernel_18444/511065402.py\", line 4, in index\n",
      "    return render_template(\"index.html\", mars=mars)\n",
      "  File \"C:\\Users\\jinna\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\templating.py\", line 138, in render_template\n",
      "    ctx.app.jinja_env.get_or_select_template(template_name_or_list),\n",
      "  File \"C:\\Users\\jinna\\anaconda3\\envs\\PythonData\\lib\\site-packages\\jinja2\\environment.py\", line 930, in get_or_select_template\n",
      "    return self.get_template(template_name_or_list, parent, globals)\n",
      "  File \"C:\\Users\\jinna\\anaconda3\\envs\\PythonData\\lib\\site-packages\\jinja2\\environment.py\", line 883, in get_template\n",
      "    return self._load_template(name, self.make_globals(globals))\n",
      "  File \"C:\\Users\\jinna\\anaconda3\\envs\\PythonData\\lib\\site-packages\\jinja2\\environment.py\", line 857, in _load_template\n",
      "    template = self.loader.load(self, name, globals)\n",
      "  File \"C:\\Users\\jinna\\anaconda3\\envs\\PythonData\\lib\\site-packages\\jinja2\\loaders.py\", line 115, in load\n",
      "    source, filename, uptodate = self.get_source(environment, name)\n",
      "  File \"C:\\Users\\jinna\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\templating.py\", line 60, in get_source\n",
      "    return self._get_source_fast(environment, template)\n",
      "  File \"C:\\Users\\jinna\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\templating.py\", line 89, in _get_source_fast\n",
      "    raise TemplateNotFound(template)\n",
      "jinja2.exceptions.TemplateNotFound: index.html\n",
      "INFO:werkzeug:127.0.0.1 - - [18/Jun/2022 16:08:23] \"\u001b[35m\u001b[1mGET / HTTP/1.1\u001b[0m\" 500 -\n",
      "INFO:werkzeug:127.0.0.1 - - [18/Jun/2022 16:08:23] \"\u001b[33mGET /favicon.ico HTTP/1.1\u001b[0m\" 404 -\n"
     ]
    }
   ],
   "source": [
    "if __name__ == \"__main__\":\n",
    "   app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f90dc978",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "PythonData",
   "language": "python",
   "name": "pythondata"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
