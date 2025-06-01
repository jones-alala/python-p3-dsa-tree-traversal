class Tree:
    def __init__(self, node):
        self.node = node

    def get_element_by_id(self, target_id):
        return self._search(self.node, target_id)

    def _search(self, current_node, target_id):
        # Check current node
        if current_node.get('id') == target_id:
            return current_node

        # Recursively check children
        for child in current_node.get('children', []):
            result = self._search(child, target_id)
            if result is not None:
                return result

        return None
