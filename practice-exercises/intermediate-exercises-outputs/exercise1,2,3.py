## Exercise 1: Data Structure Implementation

### Task: Implement a custom data structure with GitHub Copilot's assistance.

### Instructions
# 1. Create a balanced binary search tree (AVL tree)
# 2. Use detailed comments to guide implementation
# 3. Include all necessary operations

### Starting Code
# AVL Tree implementation with automatic balancing
# Supports insert, delete, search, and traversal operations
# Maintains O(log n) height through rotations
# Each node stores value, height, and left/right children
class AVLNode:
    def __init__(self, value):
        # Let Copilot initialize node properties
        self.value = value
        self.height = 1
        self.left = None
        self.right = None 
        
class AVLTree:
    def __init__(self):
        # Initialize empty tree
        self.root = None
        
    # Insert operation with automatic balancing
    # Should update heights and perform rotations as needed
    def insert(self, value):
        # Insert value into AVL tree with balancing
        def _insert(node, value):
            if not node:
                return AVLNode(value)
            if value < node.value:
                node.left = _insert(node.left, value)
            elif value > node.value:
                node.right = _insert(node.right, value)
            else:
                return node  # Duplicate values not allowed

            # Update height
            node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

            # Get balance factor
            balance = self._get_balance(node)

            # Left Left Case
            if balance > 1 and value < node.left.value:
                return self._right_rotate(node)
            # Right Right Case
            if balance < -1 and value > node.right.value:
                return self._left_rotate(node)
            # Left Right Case
            if balance > 1 and value > node.left.value:
                node.left = self._left_rotate(node.left)
                return self._right_rotate(node)
            # Right Left Case
            if balance < -1 and value < node.right.value:
                node.right = self._right_rotate(node.right)
                return self._left_rotate(node)

            return node

        self.root = _insert(self.root, value)

    # Helper methods for AVL operations
    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        return x
        
    # Delete operation maintaining AVL properties
    def delete(self, value):
        # Delete value from AVL tree with rebalancing
        def _min_value_node(node):
            current = node
            while current.left:
                current = current.left
            return current

        def _delete(node, value):
            if not node:
                return node
            if value < node.value:
                node.left = _delete(node.left, value)
            elif value > node.value:
                node.right = _delete(node.right, value)
            else:
                # Node with only one child or no child
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                temp = _min_value_node(node.right)
                node.value = temp.value
                node.right = _delete(node.right, temp.value)

            # Update height
            node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

            # Get balance factor
            balance = self._get_balance(node)

            # Left Left Case
            if balance > 1 and self._get_balance(node.left) >= 0:
                return self._right_rotate(node)
            # Left Right Case
            if balance > 1 and self._get_balance(node.left) < 0:
                node.left = self._left_rotate(node.left)
                return self._right_rotate(node)
            # Right Right Case
            if balance < -1 and self._get_balance(node.right) <= 0:
                return self._left_rotate(node)
            # Right Left Case
            if balance < -1 and self._get_balance(node.right) > 0:
                node.right = self._right_rotate(node.right)
                return self._left_rotate(node)

            return node

        self.root = _delete(self.root, value)
        
    # Search operation in O(log n) time
    def search(self, value):
        # Efficient search in AVL tree
        def _search(node, value):
            if not node:
                return False
            if value == node.value:
                return True
            elif value < node.value:
                return _search(node.left, value)
            else:
                return _search(node.right, value)
        return _search(self.root, value)
        
    # Helper methods for rotations and height calculation
    # Let Copilot suggest and implement helper methods
    #now, how to test the AVL tree implementation?
# Example usage and testing
if __name__ == "__main__":
    avl_tree = AVLTree()
    values_to_insert = [10, 20, 30, 40, 50, 25]
    for value in values_to_insert:
        avl_tree.insert(value)
    print("Day4(2/8/2026)")
    print("Exercise1-AVL Tree Search:")
    print("Search for 20:", avl_tree.search(20))  # Should return True
    print("Search for 60:", avl_tree.search(60))  # Should return False

    avl_tree.delete(20)
    print("Search for 20 after deletion:", avl_tree.search(20))  # Should return False
    avl_tree.delete(30)
    print("Search for 30 after deletion:", avl_tree.search(30))  #
    avl_tree.delete(10)
    print("Search for 10 after deletion:", avl_tree.search(10))  # Should return False
    avl_tree.delete(40)
    print("Search for 40 after deletion:", avl_tree.search(40))  # Should return False
    avl_tree.delete(50)
    print("Search for 50 after deletion:", avl_tree.search(50))  # Should return False
    avl_tree.delete(25)
    print("Search for 25 after deletion:", avl_tree.search(25))  # Should return False


## Exercise 2: Design Pattern Implementation

### Task: Implement the Observer pattern for a notification system.

### Instructions
# 1. Create a robust notification system using the Observer pattern
# 2. Use comments to specify the pattern requirements
# 3. Include type safety and error handling

### Starting Code
# Observer pattern implementation for notification system
# Publisher maintains list of subscribers and notifies them of events
# Supports multiple event types and selective subscription
from abc import ABC, abstractmethod
from typing import List, Dict, Any
from enum import Enum

class EventType(Enum):
    USER_CREATED = "user_created"
    USER_UPDATED = "user_updated"
    USER_DELETED = "user_deleted"
    ORDER_PLACED = "order_placed"

# Observer interface that all subscribers must implement
class Observer(ABC):
    @abstractmethod
    def update(self, event_type: EventType, data: Dict[str, Any]):
        pass
    
# Subject/Publisher that manages observers and sends notifications
class NotificationPublisher:
    def __init__(self):
        # Initialize observer management system
        self.observers: Dict[EventType, List[Observer]] = {event: [] for event in EventType}
        
    # Subscribe observer to specific event types
    def subscribe(self, observer: Observer, event_types: List[EventType]):
        # Subscribe observer to specific event types
        for event_type in event_types:
            if observer not in self.observers[event_type]:
                self.observers[event_type].append(observer)
        
    # Unsubscribe observer from events
    def unsubscribe(self, observer: Observer, event_types: List[EventType] = None):
        # Unsubscribe observer from events
        if event_types is None:
            # Remove observer from all event types
            for obs_list in self.observers.values():
                if observer in obs_list:
                    obs_list.remove(observer)
        else:
            for event_type in event_types:
                if observer in self.observers[event_type]:
                    self.observers[event_type].remove(observer)
        
    # Notify all relevant observers of an event
    def notify(self, event_type: EventType, data: Dict[str, Any]):
        # Notify all relevant observers of an event
        for observer in self.observers.get(event_type, []):
            try:
                observer.update(event_type, data)
            except Exception as e:
                print(f"Error notifying observer {observer}: {e}")
        
# Concrete observer implementations
class EmailNotifier(Observer):
    def update(self, event_type: EventType, data: Dict[str, Any]):
        print(f"[Email] Event: {event_type.value}, Data: {data}")
    
class SMSNotifier(Observer):
    def update(self, event_type: EventType, data: Dict[str, Any]):
        print(f"[SMS] Event: {event_type.value}, Data: {data}")
    
class DatabaseLogger(Observer):
    def update(self, event_type: EventType, data: Dict[str, Any]):
        print(f"[DB] Event: {event_type.value}, Data: {data}")

#/tests 
if __name__ == "__main__":
    publisher = NotificationPublisher()
    
    email_notifier = EmailNotifier()
    sms_notifier = SMSNotifier()
    db_logger = DatabaseLogger()
    
    publisher.subscribe(email_notifier, [EventType.USER_CREATED, EventType.ORDER_PLACED])
    publisher.subscribe(sms_notifier, [EventType.USER_UPDATED, EventType.ORDER_PLACED])
    publisher.subscribe(db_logger, list(EventType))
    
    print("\nExercise2-Notifications:")
    publisher.notify(EventType.USER_CREATED, {"user_id": 1, "name": "Alice"})
    publisher.notify(EventType.USER_UPDATED, {"user_id": 1, "name": "Alice Smith"})
    publisher.notify(EventType.ORDER_PLACED, {"order_id": 101, "user_id": 1})
    publisher.notify(EventType.USER_DELETED, {"user_id": 1})
    

## Exercise 3: Async/Await Patterns

### Task: Build an asynchronous web scraper with proper concurrency control.

### Instructions
# 1. Use async/await for concurrent HTTP requests
# 2. Implement rate limiting and error handling
# 3. Include progress tracking and result aggregation

### Starting Code
# Asynchronous web scraper with rate limiting and error handling
# Supports concurrent requests with configurable limits
# Includes retry logic, timeout handling, and progress tracking
import asyncio
import aiohttp
from typing import List, Dict, Optional
from dataclasses import dataclass
from datetime import datetime

@dataclass
class ScrapeResult:
    url: str
    content: Optional[str]
    status_code: int
    error: Optional[str]
    timestamp: datetime

# Async web scraper with advanced features
class AsyncWebScraper:
    def __init__(self, max_concurrent: int = 10, rate_limit: float = 1.0):
        # Initialize scraper with concurrency and rate limiting
        self.max_concurrent = max_concurrent
        self.rate_limit = rate_limit
        self._semaphore = asyncio.Semaphore(max_concurrent)
        
    # Scrape multiple URLs concurrently with rate limiting
    async def scrape_urls(self, urls: List[str], timeout: int = 30) -> List[ScrapeResult]:
        results: List[ScrapeResult] = []
        total = len(urls)
        completed = 0
        async with aiohttp.ClientSession() as session:
            async def scrape_and_track(url):
                nonlocal completed
                async with self._semaphore:
                    await asyncio.sleep(self.rate_limit)
                    result = await self.scrape_single_url(session, url, timeout)
                    results.append(result)
                    completed += 1
                    await self._progress_callback(completed, total)
            tasks = [scrape_and_track(url) for url in urls]
            await asyncio.gather(*tasks)
        return results
        
    # Single URL scraping with retry logic
    async def scrape_single_url(self, session: aiohttp.ClientSession, url: str, 
                                timeout: int, retries: int = 3) -> ScrapeResult:
        attempt = 0
        backoff = 1
        while attempt < retries:
            try:
                async with session.get(url, timeout=timeout) as response:
                    content = await response.text()
                    return ScrapeResult(
                        url=url,
                        content=content,
                        status_code=response.status,
                        error=None,
                        timestamp=datetime.now()
                    )
            except Exception as e:
                error_msg = str(e)
                await asyncio.sleep(backoff)
                backoff *= 2
                attempt += 1
        return ScrapeResult(
            url=url,
            content=None,
            status_code=0,
            error=error_msg,
            timestamp=datetime.now()
        )
        
    # Progress callback for tracking scraping status
    print("\nExercise3-Scraping Progress:")
    async def _progress_callback(self, completed: int, total: int):
        print(f"Scraping progress: {completed}/{total} URLs completed.")

#/tests with expeceted outputs as well as error handling for non-existent URLs
if __name__ == "__main__":
    urls_to_scrape = [
        "https://www.example.com",
        "https://www.python.org",
        "https://www.nonexistenturl.com"  # This will trigger error handling
    ]
    
    scraper = AsyncWebScraper(max_concurrent=2, rate_limit=0.5)
    results = asyncio.run(scraper.scrape_urls(urls_to_scrape))
    
    print("\nExercise3-Scraping Results:")
    for result in results:
        print(f"URL: {result.url}, Status: {result.status_code}, Error: {result.error}")
