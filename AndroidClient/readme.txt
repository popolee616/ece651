Files edited before 1st time upload:

// for network connection permission
network_security_config.xml -- dir: app\src\main\res\xml\network_security_config.xml 
AndroidManifest.xml -- dir: app/src/main/AndroidManifest.xml


//for network connecting
MainActivity.java -- dir: com/example/xinchangli/myapplication/MainActivity.java
	
	
	private class LongOperation: # a new thread(required) for message recieving
	
		/**
		Make network connection(need to change ip address everytime);
		Get message from Server
		*/
		String doinbackground(...)
		
		
		/**
		Update UI;
		Recieve the return value from  methond doinbackground() as parameter
		
		*/
		void onPostExecute(...)
		
	
