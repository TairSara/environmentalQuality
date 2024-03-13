
import { describe, test, expect, beforeEach } from "vitest";
import { shuffleQuestions } from "./scripts.js"; 

describe ('scripts', () => {
    let questions;

    beforeEach(() => {
        questions = [1, 2, 3, 4, 5];
    });

    test('should shuffle questions array', () => {
        shuffleQuestions(questions);
        expect(questions.length).toBe(5);
        expect(questions).not.toEqual([1, 2, 3, 4, 5]);
        expect([...questions].sort()).toEqual([1, 2, 3, 4, 5]);
    });    
});
