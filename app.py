import streamlit as st

# Function to read the items from the file
def file_read():
    with open("iteams.csv", "r") as file:
        return file.readlines()

# Function to write the updated items to the file
def file_write(items):
    with open("iteams.csv", "w") as file:
        file.writelines(items)

st.markdown(
    """
    <style>
    body {
        font-size: 32px;  /* Default text size */
    }
    h1 {
        font-size: 56px;  /* Title */
    }
    h2 {
        font-size: 48px;  /* Header */
    }
    .stButton>button {
        font-size: 30px;  /* Button text */
    }
    .stTextInput>input {
        font-size: 30px;  /* Text input */
    }
    .stSelectbox>div>div {
        font-size: 30px;  /* Selectbox */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main application layout
def main():
    st.title("Welcome to Happy Coding!")

    # Sidebar with buttons for navigation
    st.sidebar.title("Operations")
    option = st.sidebar.radio(
        "Choose an option", ["Show Items", "Add Item", "Edit Item", "Delete Item"]
    )

    # Show Items
    if option == "Show Items":
        st.subheader("Current Items:")
        prajju = file_read()
        if prajju:
            for id, item in enumerate(prajju, start=1):
                st.write(f"{id}. {item.strip()}")
        else:
            st.write("No items found!")

    # Add Item
    elif option == "Add Item":
        st.subheader("Add a New Item")
        item_input = st.text_input("Enter the item name and price (separated by space):")

        if st.button("Add Item"):
            if item_input:
                prajju = file_read()
                index = len(prajju) + 1  # New index for the item
                prajju.append(f"{index}. {item_input}\n")
                file_write(prajju)
                st.success(f"Item '{item_input}' added successfully!")
            else:
                st.error("Please enter a valid item and price!")

    # Edit Item
    elif option == "Edit Item":
        st.subheader("Edit an Item")
        prajju = file_read()
        if prajju:
            item_ids = [str(id + 1) for id, _ in enumerate(prajju)]
            item_to_edit = st.selectbox("Choose an item to edit", item_ids)

            if item_to_edit:
                id_to_edit = int(item_to_edit) - 1
                current_item = prajju[id_to_edit].strip()

                new_item = st.text_input("Enter the new item and price:", value=current_item)

                if st.button("Update Item"):
                    prajju[id_to_edit] = f"{id_to_edit + 1}. {new_item}\n"
                    file_write(prajju)
                    st.success(f"Item '{current_item}' updated successfully to '{new_item}'!")
        else:
            st.write("No items found!")

    # Delete Item
    elif option == "Delete Item":
        st.subheader("Delete an Item")
        prajju = file_read()
        if prajju:
            item_ids = [str(id + 1) for id, _ in enumerate(prajju)]
            item_to_delete = st.selectbox("Choose an item to delete", item_ids)

            if item_to_delete:
                id_to_delete = int(item_to_delete) - 1
                current_item = prajju[id_to_delete].strip()

                if st.button("Delete Item"):
                    prajju.pop(id_to_delete)
                    file_write(prajju)
                    st.success(f"Item '{current_item}' deleted successfully!")
        else:
            st.write("No items found!")

# Run the app
if __name__ == "__main__":
    main()
