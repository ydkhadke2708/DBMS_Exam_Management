
Create Database Exam;
Use Exam;
create table department
	(	
		dep_name		varchar(30),
		building      	varchar(30),
		budget 			numeric(12),
		primary key (dep_name)
	);

create table student
	( id		varchar(10),
	  name		varchar(30),
	  email		varchar(30),
	  dep      varchar(30),
	  DOB 		varchar(20),
	  gender      varchar(6),
	  pass		varchar(30) not null,
	  sem 		varchar(1),
	  flag 		varchar(1),
	 primary key (id),
	 foreign key (dep) references department(dep_name) 
	 		on delete cascade
	);
	
create table professor
	( id			varchar(10),
	  name		varchar(30),
	  email		varchar(30),
	  dep      varchar(30),
	  DOB 		varchar(20),
	  gender      varchar(6),
	  pass		varchar(30) not null,
	 primary key (id),
	 foreign key (dep) references department(dep_name) on delete cascade
	);
	
create table administrator
	( id			varchar(10),
	  name		varchar(30),
	  email		varchar(30),
	  DOB 		varchar(20),
	  gender      varchar(6),
	  pass		varchar(30) not null,
	 primary key (id)
	);
	
create table course
	(	id			varchar(10),
		name		varchar(30),
		dep      	varchar(30),
		credits 	numeric(2),
		primary key (id),
		foreign key (dep) references department(dep_name) on delete cascade
	);
	
create table teaches
	(	course_id 	varchar(10),
		prof_id 	varchar(10),
		semester	varchar(1),
		primary key (course_id , prof_id ,semester),
		foreign key (course_id) references course(id) on delete cascade,
		foreign key (prof_id) references professor(id) on delete cascade
	);

create table enrolled
	(	course_id 	varchar(10),
		s_id 	varchar(10),
		sem		varchar(1),
		attendance varchar(5),
		primary key (course_id , s_id ,sem),
		foreign key (course_id) references course(id) on delete cascade,
		foreign key (s_id) references student(id) on delete cascade
		
	);	
		
create table fees
	(  	s_id 		varchar(10),
		ID			varchar(20),
		amount		numeric(10),
		semester	varchar(1),
		primary key (s_id , semester),
		foreign key (s_id) references student(id) on delete cascade
	);

create table feedback
	(	s_id		varchar(10),
		prof_id		varchar(10),
		sem			varchar(1),
		course_id 	varchar(10),
		message 	varchar(200),
		primary key (s_id , prof_id , sem , course_id) ,
		foreign key (s_id) references student(id) on delete cascade,
		foreign key (course_id) references course(id) on delete cascade,
		foreign key (prof_id) references professor(id) on delete cascade
		
	);
	
create table exam
	(	exam_id varchar(10),
		course_id 	varchar(10),
		sem			varchar(1),
		d_ate	varchar(10),
		time	varchar(20),
		classroom	varchar(20),
		supervisor varchar(10),
		primary key (exam_id),
		foreign key (course_id) references course(id) on delete cascade,
		foreign key (supervisor) references professor(id) on delete cascade
	);
	
create table result 
	(	exam_id varchar(10),
		s_id 	varchar(10),
		grade 	numeric(10),
		
		primary key (exam_id,s_id),
		foreign key (exam_id) references exam(exam_id) on delete cascade,
		foreign key (s_id) references student(id) on delete cascade
	);

		
Insert into administrator values( "9403836118" , "Abhijeet" , "admin.comp@coep.ac.in","27/08/01" , "MALE","Admin");

Insert into department values("Computer Engineering" , "Main Building" , 60000);
Insert into department values("ENTC" , "ENTC Building" , 50000);
Insert into department values("Civil Engineering" , "Civil Building" , 50000);
Insert into department values("Mechanical Engineering" , "Mechanical Building" , 60000);
Insert into department values("Chemical Engineering" , "Main Building" , 60000);

Insert into student values("111903131" , "Yadnyadeep Khadke" , "khadkeyn19.comp@coep.ac.in" , "Computer Engineering" ,"22/05/01" ,"MALE" ,"Coep1234" ,"4" , "0");
Insert into student values("111903130" , "Vrushabh Patil" , "patilvp19.comp@coep.ac.in" , "Computer Engineering" ,"22/05/01" ,"MALE" ,"Coep1234" ,"4" , "0");
Insert into student values("111903127" , "Viraj Najan" , "najanvd19.comp@coep.ac.in" , "Computer Engineering" ,"22/05/01" ,"MALE" ,"Coep1234" ,"4", "0");
Insert into student values("111903133" , "Abhay Koushal" , "koushala19.comp@coep.ac.in" , "Computer Engineering" ,"22/05/01" ,"MALE" ,"Coep1234" ,"4" , "0");
Insert into student values("111903125" , "Vipin Ingle" , "inglevp19.comp@coep.ac.in" , "Computer Engineering" ,"22/05/01" ,"MALE" ,"Coep1234" ,"4" , "0");
Insert into student values("111903126" , "Vipul Gaikwad" , "gaikwadvl19.comp@coep.ac.in" , "Computer Engineering" ,"22/05/01" ,"MALE" ,"Coep1234" ,"4" , "0");
Insert into student values("111903129" , "Vivek Bhand" , "bhandvv19.comp@coep.ac.in" , "Computer Engineering" ,"22/05/01" ,"MALE" ,"Coep1234" ,"4" , "0");
Insert into student values("111903134" , "Aditya Verma" , "vermaar19.comp@coep.ac.in" , "Computer Engineering" ,"22/05/01" ,"MALE" ,"Coep1234" ,"4" , "0");
Insert into student values("111903137" , "Anjali Dofe " , "dofeaa19.comp@coep.ac.in" , "Computer Engineering" ,"22/05/01" ,"FEMALE" ,"Coep1234" ,"4" , "0");
Insert into student values("111903123" , "Vidhi Shah" , "shahvr19.comp@coep.ac.in" , "Computer Engineering" ,"22/05/01" ,"FEMALE" ,"Coep1234" ,"4" , "0");
Insert into student values("111903124" , "Vinaysingh Patil" , "patilvinayp19.comp@coep.ac.in" , "Computer Engineering" ,"22/05/01" ,"MALE" ,"Coep1234" ,"4" , "0");
Insert into student values("111903132" , "Yashwant Ingle" , "ingleye19.comp@coep.ac.in" , "Computer Engineering" ,"22/05/01" ,"MALE" ,"Coep1234" ,"4" , "0");
Insert into student values("111903121" , "Vedant Baigragi" , "bairagivg19.comp@coep.ac.in" , "Computer Engineering" ,"22/05/01" ,"MALE" ,"Coep1234" ,"4" , "0");
Insert into student values("111903122" , "Vedashree Satpute" , "satputevs19.comp@coep.ac.in" , "Computer Engineering" ,"22/05/01" ,"FEMALE" ,"Coep1234" ,"4" , "0");
Insert into student values("111903136" , "Ambar Kumar" , "kumara19.comp@coep.ac.in" , "Computer Engineering" ,"22/05/01" ,"MALE" ,"Coep1234" ,"4" , "0");
Insert into student values("111903128" , "Vishwajit Kadam" , "kadamvv19.comp@coep.ac.in" , "Computer Engineering" ,"22/05/01" ,"MALE" ,"Coep1234" ,"4" , "0");
Insert into student values("111903135" , "Aman Patil" , "patilaj19.comp@coep.ac.in" , "Computer Engineering" ,"22/05/01" ,"MALE" ,"Coep1234" ,"4" , "0");
Insert into student values("111903199" , "Virat Kholi" , "kholiv19.comp@coep.ac.in" , "Computer Engineering" ,"22/05/01" ,"MALE" ,"Coep1234" ,"4" , "0");
Insert into student values("111903198" , "Rohit Sharma" , "sharmar19.comp@coep.ac.in" , "Computer Engineering" ,"22/05/01" ,"MALE" ,"Coep1234" ,"4" , "0");
Insert into fees values("111903121" , "NULL" , 0 ,4);
Insert into fees values("111903122" , "NULL" , 0 , 4);
Insert into fees values("111903123" , "NULL" , 0 , 4);
Insert into fees values("111903124" , "NULL" , 0 , 4);
Insert into fees values("111903125" , "NULL" , 0 ,4 );
Insert into fees values("111903126" , "NULL" , 0 , 4);

Insert into fees values("111903127" , "NULL" , 0 ,4);
Insert into fees values("111903128" , "NULL" , 0 , 4);
Insert into fees values("111903129" , "NULL" , 0 ,4 );
Insert into fees values("111903130" , "NULL" , 0 ,4 );
Insert into fees values("111903131" , "NULL" , 0 ,4);

Insert into fees values("111903132" , "NULL" , 0 , 4);
Insert into fees values("111903133" , "NULL" , 0 , 4);
Insert into fees values("111903134" , "NULL" , 0 , 4);

Insert into fees values("111903135" , "NULL" , 0 , 4);
Insert into fees values("111903136" , "NULL" , 0 , 4);
Insert into fees values("111903137" , "NULL" , 0 , 4);
Insert into fees values("111903199" , "NULL" , 0 , 4);
Insert into fees values("111903198" , "NULL" , 0 , 4);


Insert into course values("D_S_A" , "DSA" ,"Computer Engineering" , "3" );
Insert into course values("C_N" , "CN" ,"Computer Engineering" , "3" );

Insert into course values("A_I" , "AI" ,"Computer Engineering" , "3" );
Insert into course values("P_S_E" , "Probability" ,"Computer Engineering" , "3" );
Insert into course values("T_O_C" , "Theory of Computation" ,"Computer Engineering" , "3" );
Insert into course values("D_C" , "Data Communication" ,"Computer Engineering" , "3" );
Insert into course values("P_P_S" , "Programming" ,"Computer Engineering" , "3" );
Insert into course values("D_L" , "Digital_Logic" ,"Computer Engineering" , "3" );
Insert into course values("O_D_E" , "Ordinary Differnetial Eqn" ,"Computer Engineering" , "3" );
Insert into course values("C_O" , "Comouter Organization" ,"Computer Engineering" , "3" );
Insert into course values("MPT" , "Micro Processors" ,"Computer Engineering" , "3" );
Insert into course values("RPPOOP" , "Rapid Object Oriented" ,"Computer Engineering" , "3" );
Insert into course values("S_E" , "Software Engineering" ,"Computer Engineering" , "3" );
Insert into course values("LA" , "Linear Algebra" ,"Computer Engineering" , "3" );
Insert into course values("EMWA" , "ElectroMagnetic Waves" ,"ENTC" , "3" );
Insert into course values("CLPD" , "Configurable Logic " ,"ENTC" , "3" );
Insert into course values("DSP" , "Digital Signal Process" ,"ENTC" , "3" );
Insert into course values("DC" , "Digital Communication" ,"ENTC" , "3" );
Insert into course values("RPP" , "R and Python Programming" ,"ENTC" , "3" );
Insert into course values("FM" , "Fluid Machinery" ,"Mechanical Engineering" , "3" );
Insert into course values("MMM" , "Metrology Mechanical" ,"Mechanical Engineering" , "3" );
Insert into course values("HT" , "Heat Transfer" ,"Mechanical Engineering" , "3" );
Insert into course values("DMC" , "Design Machine Components" ,"Mechanical Engineering" , "3" );
Insert into course values("TE" , "Transportation Engg" ,"Civil Engineering" , "3" );
Insert into course values("LWM" , "Land Water Management" ,"Civil Engineering" , "3" );

Insert into professor values("11115" , "Ashwini Matange" , "matange14@coep.ac.in" , "Computer Engineering" ,"22/05/01" ,"FEMALE" ,"Coep1234");
Insert into teaches values("D_S_A" , "11115" , "3" );
Insert into enrolled values("D_S_A" , "111903121" , "3" , "90%" );
Insert into enrolled values("D_S_A" , "111903122" , "3" , "90%" );
Insert into enrolled values("D_S_A" , "111903123" , "3" , "90%" );
Insert into enrolled values("D_S_A" , "111903124" , "3" , "90%" );
Insert into enrolled values("D_S_A" , "111903125" , "3" , "90%" );
Insert into enrolled values("D_S_A" , "111903126" , "3" , "90%" );
Insert into enrolled values("D_S_A" , "111903127" , "3" , "90%" );
Insert into enrolled values("D_S_A" , "111903128" , "3" , "90%" );
Insert into enrolled values("D_S_A" , "111903129" , "3" , "90%" );
Insert into enrolled values("D_S_A" , "111903130" , "3" , "90%" );
Insert into enrolled values("D_S_A" , "111903131" , "3" , "90%" );
Insert into enrolled values("D_S_A" , "111903132" , "3" , "90%" );
Insert into enrolled values("D_S_A" , "111903133" , "3" , "90%" );
Insert into enrolled values("D_S_A" , "111903134" , "3" , "90%" );
Insert into enrolled values("D_S_A" , "111903135" , "3" , "90%" );
Insert into enrolled values("D_S_A" , "111903136" , "3" , "90%" );
Insert into enrolled values("D_S_A" , "111903137" , "3" , "90%" );
Insert into enrolled values("D_S_A" , "111903199" , "3" , "90%" );
Insert into enrolled values("D_S_A" , "111903198" , "3" , "90%" );

Insert into professor values("11111" , "J.B.Abhraham" , "jbabharam14@coep.ac.in" , "Computer Engineering" ,"22/05/01" ,"FEMALE" ,"Coep1234");
Insert into teaches values("T_O_C" , "11111" , "3" );
Insert into enrolled values("T_O_C", "111903131" , "3" , "99%");
Insert into enrolled values("T_O_C", "111903130" , "3" , "99%");

Insert into professor values("11112" , "Deepak Kshirsagar" , "dkshirsagar14@coep.ac.in" , "Computer Engineering" ,"22/05/01" ,"MALE" ,"Coep1234");
Insert into teaches values("D_C" , "11112" , "3" );
Insert into enrolled values("D_C", "111903131" , "3" , "99%");
Insert into enrolled values("D_C", "111903130" , "3" , "99%");

Insert into professor values("11113" , "Jagruti Mam" , "jagruti14@coep.ac.in" , "Computer Engineering" ,"22/05/01" ,"FEMALE" ,"Coep1234");
Insert into teaches values("D_L" , "11113" , "3" );
Insert into enrolled values("D_L", "111903131" , "3" , "99%");
Insert into enrolled values("D_L", "111903130" , "3" , "99%");

Insert into professor values("11114" , "Yogita Mam" , "ymahatekar14@coep.ac.in" , "Computer Engineering" ,"22/05/01" ,"FEMALE" ,"Coep1234");
Insert into teaches values("O_D_E" , "11114" , "3" );
Insert into enrolled values("O_D_E", "111903131" , "3" , "99%");
Insert into enrolled values("O_D_E", "111903130" , "3" , "99%");


Insert into teaches values("D_S_A" , "11115" , "4" );
Insert into enrolled values("D_S_A", "111903131" , "4" , "99%");
Insert into enrolled values("D_S_A", "111903130" , "4" , "99%");

Insert into professor values("11116" , "Arun Sawant" , "sawantarun14@coep.ac.in" , "Computer Engineering" ,"22/05/01" ,"FEMALE" ,"Coep1234");
Insert into teaches values("C_O" , "11116" , "4" );
Insert into enrolled values("C_O", "111903131" , "4" , "99%");
Insert into enrolled values("C_O", "111903130" , "4" , "99%");

Insert into teaches values("P_P_S" , "11113" , "4" );
Insert into enrolled values("P_P_S", "111903131" , "4" , "99%");
Insert into enrolled values("P_P_S", "111903130" , "4" , "99%");

Insert into teaches values("MPT" , "11116" , "4" );
Insert into enrolled values("MPT", "111903131" , "4" , "99%");
Insert into enrolled values("MPT", "111903130" , "4" , "99%");


Insert into teaches values("RPPOOP" , "11112" , "4" );
Insert into enrolled values("RPPOOP", "111903131" , "4" , "99%");
Insert into enrolled values("RPPOOP", "111903130" , "4" , "99%");




