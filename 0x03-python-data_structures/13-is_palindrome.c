#include "lists.h"

/**
 * checkPalindrome - recursive function for checking palindrome
 * @left: node
 * @right: node
 * Return: 1 if palindrome, 0 otherwise
 */

int checkPalindrome(listint_t **left, listint_t *right)
{
	int res = 0;

	if (right == NULL)
		return (1);

	res = checkPalindrome(left, right->next) &&
		((*left)->n == right->n);
	(*left) = (*left)->next;

	return (res);
}
/**
 * is_palindrome - call the above function
 * @head: head of a list
 * Return: 1 if palindome, 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	if (*head == NULL)
		return (1);
	return (checkPalindrome(&(*head), *head));
}
