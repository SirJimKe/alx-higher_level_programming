#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: double pointer to head node
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev_slow = NULL;
	listint_t *mid = NULL;
	listint_t *second_half = slow;
	listint_t *prev = NULL;
	listint_t *current = second_half;
	listint_t *next = NULL;
	listint_t *p1 = *head;
	listint_t *p2 = second_half;

	if (*head == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}

	if (fast != NULL)
	{
		mid = slow;
		slow = slow->next;
	}

	prev_slow->next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	second_half = prev;


	while (p1 != NULL && p2 != NULL)
	{
		if (p1->n != p2->n)
			return (0);

		p1 = p1->next;
		p2 = p2->next;
	}

	prev = NULL;
	current = second_half;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	second_half = prev;

	if (mid != NULL)
	{
		prev_slow->next = mid;
		mid->next = second_half;
	}
	else
		prev_slow->next = second_half;

	return (1);
}
