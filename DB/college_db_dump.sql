--
-- PostgreSQL database dump
--

\restrict 3DyEmCKUbAdzvpWc247HUFNLHzDc7SPSewhhEscUKQESsuAcnNL6vPtivbPVTjC

-- Dumped from database version 18.1
-- Dumped by pg_dump version 18.1

-- Started on 2026-06-14 17:59:48

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 224 (class 1259 OID 68557)
-- Name: courses; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.courses (
    course_id integer NOT NULL,
    course_name character varying(150) NOT NULL,
    course_code character varying(20),
    credits integer,
    department_id integer
);


ALTER TABLE public.courses OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 68556)
-- Name: courses_course_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.courses_course_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.courses_course_id_seq OWNER TO postgres;

--
-- TOC entry 5064 (class 0 OID 0)
-- Dependencies: 223
-- Name: courses_course_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.courses_course_id_seq OWNED BY public.courses.course_id;


--
-- TOC entry 220 (class 1259 OID 68530)
-- Name: departments; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.departments (
    department_id integer NOT NULL,
    dept_name character varying(100) NOT NULL,
    hod_name character varying(100),
    budget numeric(12,2)
);


ALTER TABLE public.departments OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 68529)
-- Name: departments_department_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.departments_department_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.departments_department_id_seq OWNER TO postgres;

--
-- TOC entry 5065 (class 0 OID 0)
-- Dependencies: 219
-- Name: departments_department_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.departments_department_id_seq OWNED BY public.departments.department_id;


--
-- TOC entry 226 (class 1259 OID 68573)
-- Name: enrollments; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.enrollments (
    enrollment_id integer NOT NULL,
    student_id integer,
    course_id integer,
    enrollment_date date,
    grade character(2)
);


ALTER TABLE public.enrollments OWNER TO postgres;

--
-- TOC entry 225 (class 1259 OID 68572)
-- Name: enrollments_enrollment_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.enrollments_enrollment_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.enrollments_enrollment_id_seq OWNER TO postgres;

--
-- TOC entry 5066 (class 0 OID 0)
-- Dependencies: 225
-- Name: enrollments_enrollment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.enrollments_enrollment_id_seq OWNED BY public.enrollments.enrollment_id;


--
-- TOC entry 228 (class 1259 OID 68591)
-- Name: professors; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.professors (
    professor_id integer NOT NULL,
    prof_name character varying(100) NOT NULL,
    email character varying(100),
    department_id integer,
    salary numeric(10,2)
);


ALTER TABLE public.professors OWNER TO postgres;

--
-- TOC entry 227 (class 1259 OID 68590)
-- Name: professors_professor_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.professors_professor_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.professors_professor_id_seq OWNER TO postgres;

--
-- TOC entry 5067 (class 0 OID 0)
-- Dependencies: 227
-- Name: professors_professor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.professors_professor_id_seq OWNED BY public.professors.professor_id;


--
-- TOC entry 222 (class 1259 OID 68539)
-- Name: students; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.students (
    student_id integer NOT NULL,
    first_name character varying(50) NOT NULL,
    last_name character varying(50) NOT NULL,
    email character varying(100) NOT NULL,
    date_of_birth date,
    department_id integer,
    enrollment_year integer
);


ALTER TABLE public.students OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 68538)
-- Name: students_student_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.students_student_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.students_student_id_seq OWNER TO postgres;

--
-- TOC entry 5068 (class 0 OID 0)
-- Dependencies: 221
-- Name: students_student_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.students_student_id_seq OWNED BY public.students.student_id;


--
-- TOC entry 4878 (class 2604 OID 68560)
-- Name: courses course_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.courses ALTER COLUMN course_id SET DEFAULT nextval('public.courses_course_id_seq'::regclass);


--
-- TOC entry 4876 (class 2604 OID 68533)
-- Name: departments department_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.departments ALTER COLUMN department_id SET DEFAULT nextval('public.departments_department_id_seq'::regclass);


--
-- TOC entry 4879 (class 2604 OID 68576)
-- Name: enrollments enrollment_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.enrollments ALTER COLUMN enrollment_id SET DEFAULT nextval('public.enrollments_enrollment_id_seq'::regclass);


--
-- TOC entry 4880 (class 2604 OID 68594)
-- Name: professors professor_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.professors ALTER COLUMN professor_id SET DEFAULT nextval('public.professors_professor_id_seq'::regclass);


--
-- TOC entry 4877 (class 2604 OID 68542)
-- Name: students student_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.students ALTER COLUMN student_id SET DEFAULT nextval('public.students_student_id_seq'::regclass);


--
-- TOC entry 5054 (class 0 OID 68557)
-- Dependencies: 224
-- Data for Name: courses; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.courses (course_id, course_name, course_code, credits, department_id) FROM stdin;
1	Data Structures & Algorithms	CS101	4	1
2	Database Management Systems	CS102	3	1
3	Object Oriented Programming	CS103	4	1
4	Circuit Theory	EC101	3	2
5	Thermodynamics	ME101	3	3
\.


--
-- TOC entry 5050 (class 0 OID 68530)
-- Dependencies: 220
-- Data for Name: departments; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.departments (department_id, dept_name, hod_name, budget) FROM stdin;
1	Computer Science	Dr. Ramesh Kumar	850000.00
2	Electronics	Dr. Priya Nair	620000.00
3	Mechanical	Dr. Suresh Iyer	540000.00
4	Civil	Dr. Ananya Sharma	430000.00
\.


--
-- TOC entry 5056 (class 0 OID 68573)
-- Dependencies: 226
-- Data for Name: enrollments; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.enrollments (enrollment_id, student_id, course_id, enrollment_date, grade) FROM stdin;
1	1	1	2022-07-01	A 
2	1	2	2022-07-01	B 
3	2	1	2022-07-01	B 
4	2	3	2022-07-01	A 
5	3	4	2021-07-01	A 
6	4	5	2023-07-01	\N
7	5	1	2022-07-01	C 
8	5	2	2022-07-01	A 
9	6	4	2021-07-01	B 
10	7	5	2023-07-01	\N
11	8	1	2022-07-01	A 
12	8	3	2022-07-01	B 
\.


--
-- TOC entry 5058 (class 0 OID 68591)
-- Dependencies: 228
-- Data for Name: professors; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.professors (professor_id, prof_name, email, department_id, salary) FROM stdin;
1	Dr. Anand Krishnan	anand.k@college.edu	1	95000.00
2	Dr. Meena Pillai	meena.p@college.edu	1	88000.00
3	Dr. Sunil Rajan	sunil.r@college.edu	2	82000.00
4	Dr. Latha Gopal	latha.g@college.edu	3	79000.00
5	Dr. Kartik Bose	kartik.b@college.edu	4	76000.00
\.


--
-- TOC entry 5052 (class 0 OID 68539)
-- Dependencies: 222
-- Data for Name: students; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.students (student_id, first_name, last_name, email, date_of_birth, department_id, enrollment_year) FROM stdin;
1	Arjun	Mehta	arjun.mehta@college.edu	2003-04-12	1	2022
2	Priya	Suresh	priya.suresh@college.edu	2003-07-25	1	2022
3	Rohan	Verma	rohan.verma@college.edu	2002-11-08	2	2021
4	Sneha	Patel	sneha.patel@college.edu	2004-01-30	3	2023
5	Vikram	Das	vikram.das@college.edu	2003-09-14	1	2022
6	Kavya	Menon	kavya.menon@college.edu	2002-05-17	2	2021
7	Aditya	Singh	aditya.singh@college.edu	2004-03-22	4	2023
8	Deepika	Rao	deepika.rao@college.edu	2003-08-09	1	2022
\.


--
-- TOC entry 5069 (class 0 OID 0)
-- Dependencies: 223
-- Name: courses_course_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.courses_course_id_seq', 5, true);


--
-- TOC entry 5070 (class 0 OID 0)
-- Dependencies: 219
-- Name: departments_department_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.departments_department_id_seq', 4, true);


--
-- TOC entry 5071 (class 0 OID 0)
-- Dependencies: 225
-- Name: enrollments_enrollment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.enrollments_enrollment_id_seq', 12, true);


--
-- TOC entry 5072 (class 0 OID 0)
-- Dependencies: 227
-- Name: professors_professor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.professors_professor_id_seq', 5, true);


--
-- TOC entry 5073 (class 0 OID 0)
-- Dependencies: 221
-- Name: students_student_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.students_student_id_seq', 8, true);


--
-- TOC entry 4888 (class 2606 OID 68566)
-- Name: courses courses_course_code_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.courses
    ADD CONSTRAINT courses_course_code_key UNIQUE (course_code);


--
-- TOC entry 4890 (class 2606 OID 68564)
-- Name: courses courses_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.courses
    ADD CONSTRAINT courses_pkey PRIMARY KEY (course_id);


--
-- TOC entry 4882 (class 2606 OID 68537)
-- Name: departments departments_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.departments
    ADD CONSTRAINT departments_pkey PRIMARY KEY (department_id);


--
-- TOC entry 4892 (class 2606 OID 68579)
-- Name: enrollments enrollments_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.enrollments
    ADD CONSTRAINT enrollments_pkey PRIMARY KEY (enrollment_id);


--
-- TOC entry 4894 (class 2606 OID 68600)
-- Name: professors professors_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.professors
    ADD CONSTRAINT professors_email_key UNIQUE (email);


--
-- TOC entry 4896 (class 2606 OID 68598)
-- Name: professors professors_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.professors
    ADD CONSTRAINT professors_pkey PRIMARY KEY (professor_id);


--
-- TOC entry 4884 (class 2606 OID 68550)
-- Name: students students_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.students
    ADD CONSTRAINT students_email_key UNIQUE (email);


--
-- TOC entry 4886 (class 2606 OID 68548)
-- Name: students students_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.students
    ADD CONSTRAINT students_pkey PRIMARY KEY (student_id);


--
-- TOC entry 4898 (class 2606 OID 68567)
-- Name: courses courses_department_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.courses
    ADD CONSTRAINT courses_department_id_fkey FOREIGN KEY (department_id) REFERENCES public.departments(department_id);


--
-- TOC entry 4899 (class 2606 OID 68585)
-- Name: enrollments enrollments_course_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.enrollments
    ADD CONSTRAINT enrollments_course_id_fkey FOREIGN KEY (course_id) REFERENCES public.courses(course_id);


--
-- TOC entry 4900 (class 2606 OID 68580)
-- Name: enrollments enrollments_student_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.enrollments
    ADD CONSTRAINT enrollments_student_id_fkey FOREIGN KEY (student_id) REFERENCES public.students(student_id);


--
-- TOC entry 4901 (class 2606 OID 68601)
-- Name: professors professors_department_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.professors
    ADD CONSTRAINT professors_department_id_fkey FOREIGN KEY (department_id) REFERENCES public.departments(department_id);


--
-- TOC entry 4897 (class 2606 OID 68551)
-- Name: students students_department_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.students
    ADD CONSTRAINT students_department_id_fkey FOREIGN KEY (department_id) REFERENCES public.departments(department_id);


-- Completed on 2026-06-14 17:59:48

--
-- PostgreSQL database dump complete
--

\unrestrict 3DyEmCKUbAdzvpWc247HUFNLHzDc7SPSewhhEscUKQESsuAcnNL6vPtivbPVTjC

