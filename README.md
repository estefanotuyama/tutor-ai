# Project Synapse

A RAG-powered AI tutor for Harvard's CS50 course, allowing users to ask questions and get timestamped answers directly from the 25-hour lecture.

## The Problem

Navigating dense, long-form educational content like university lectures is challenging. Finding a specific concept or answer within a 25-hour video is time-consuming and inefficient, making it difficult to review and study the material effectively.

## The Solution

Project Synapse ingests the complete transcript of the Harvard CS50 lecture and uses a Retrieval-Augmented Generation (RAG) pipeline to create an intelligent Q&A system. It allows users to ask questions in natural language and receive concise answers grounded in the course material, complete with a direct link to the specific moment in the video where the topic was discussed.

## Tech Stack (Planned)

* **Language:** Python
* **API:** FastAPI (soon)
* **Database:** Weaviate (Vector Database)
* **AI:** LLM yet to be defined - currently using deepseek r1 1.5b

## Project Status

> 🚧 This project is in the initial development phase.