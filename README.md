# ETL-Pipeline
Api (live data) - GCP cloud - Data Fusion - Big querry - Looker Studio visualisation - Cloud composer - Apache Airflow .

* 1st step :
  In This project i fetched API cars live  data from  ( https://rapidapi.com/hub )  website.
  code consist of
           api code part
           pass key part
           google cloud connection to bucket part
           data count part
           csv save local and too bucket part
* 2nd step :
  I created a Bucket in GCP cloud and  installed google cloud sdk .and done cli setup in local terminal . and environment up.

* 3rd step :
  After running the code again with bucket id .it saved the fetched data csv in bucket.

* 4th step :
  Data fusion: i created an  instance with small and coonected to the data . Transformed the data in data fusion action wrangler  removing coloumns, null values ,splitting coloumn ,renaming columns . 
  conected the pipeline ------- Gcp bucket -----Data fusion ------Big querry. Big querry is selected from the sink wrangler library.

* 5th step :
  Big querry : created a Big querry table name and all.afterward it will create a data table.

* 6th step :
  Looker studio : login with your google account . search the option connect to big querry , locate the file . connect the data.
  visualisation will be done as the user story.

*7th step :
  Making automated process 
  cloud composer : create an environment  

*8th step :
  write the code of airflow and Dag .save it to the bucket.
   code : airflow part
          reconnect part
          timer part
          dag part
          e-mail if airflow failed part

9th step :
  airflow : dag will appear on airflow . run it .if it succeed. it started the automated process.

10th step : if it is failed for libraries & pip.
            in composer u can find pyps packages . create the package(pip) wahat to be installed name .

Run the airflow again.

For Reference video : https://www.youtube.com/watch?v=kxV4_xDchCc&list=PLLrA_pU9-Gz2DaQDcY5g9aYczmipBQ_Ek&index=2
