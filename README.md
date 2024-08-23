# ETL-Pipeline
Api (live data) - GCP cloud - Data Fusion - Big querry - Looker Studio visualisation .

* 1st step
  In This project i fetched API cars live  data from  ( https://rapidapi.com/hub )  website.
  code consist of
           api code
           pass key
           google cloud connection to bucket
           data count
           csv save local and too bucket
*2nd step
  I created a Bucket in GCP cloud and  installed google cloud sdk .and done cli setup in local terminal . and environment up.

*3rd step 
  After running the code again with bucket id .it saved the fetched data csv in bucket.

*4th step 
  Data fusion: i created an  instance with small and coonected to the data . Transformed the data in data fusion action wrangler  removing coloumns, null values ,splitting coloumn ,renaming columns . 
  conected the pipeline ------- Gcp bucket -----Data fusion ------Big querry. Big querry is selected from the sink wrangler library.

*5th step
  Big querry : created a Big querry table name and all.afterward it will create a data table.

*6th step 
 Looker studio : login with your google account . search the option connect to big querry , locate the file . connect the data.
 visualisation will be done as the user story. 
