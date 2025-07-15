# #!/bin/bash

# echo "🚀 Running Student API Tests on http://localhost:5000"
# echo "======================================="

# # Health Check
# echo "🔍 Health Check"
# curl -s -X GET http://localhost:5000/health -w "\nStatus: %{http_code}\n\n"

# # Create Students
# echo "➕ Creating Students"
# curl -s -X POST http://localhost:5000/students \
#   -H "Content-Type: application/json" \
#   -d '{"name": "John Doe", "age": 20, "email": "john@example.com"}' \
#   -w "\nStatus: %{http_code}\n\n"

# curl -s -X POST http://localhost:5000/students \
#   -H "Content-Type: application/json" \
#   -d '{"name": "Jane Smith", "age": 22, "email": "jane@example.com", "interests": ["ML"], "achievements": ["Topper"], "courses": ["AI"]}' \
#   -w "\nStatus: %{http_code}\n\n"

# # Read All Students
# echo "📖 Fetching All Students"
# curl -s -X GET http://localhost:5000/students -w "\nStatus: %{http_code}\n\n"

# # Get student by id
# echo "📄 Fetching Student by ID (should be Jane Smith)..."
# curl -s -X GET http://localhost:5000/students/2 | jq
# echo -e "\n"

# # Update Student
# echo "✏️ Updating Student 1"
# curl -s -X PUT http://localhost:5000/students/1 \
#   -H "Content-Type: application/json" \
#   -d '{"name": "Updated John", "age": 21}' \
#   -w "\nStatus: %{http_code}\n\n"

# # AI Summary
# echo "🧠 Generating Summary for Student 2"
# curl -s -X GET http://localhost:5000/students/2/summary -w "\nStatus: %{http_code}\n\n"

# # Concurrency Test: Create Multiple Students Simultaneously
# echo "🔄 Creating 5 Students Concurrently..."
# for i in {1..5}; do
#   curl -s -X POST http://localhost:5000/students \
#     -H "Content-Type: application/json" \
#     -d "{\"name\": \"Concurrent Student $i\", \"age\": $((18+i)), \"email\": \"c$i@example.com\"}" \
#     -w " [C$i: %{http_code}]" &
# done
# wait
# echo -e "\n✅ All concurrent student creation requests completed.\n"

# # Mixed Concurrent Operations
# echo "🔃 Running Mixed Concurrent Operations..."
# curl -s -X GET http://localhost:5000/students/2 &
# curl -s -X PUT http://localhost:5000/students/2 \
#   -H "Content-Type: application/json" \
#   -d '{"email": "updated2@example.com"}' &
# curl -s -X GET http://localhost:5000/students &
# curl -s -X POST http://localhost:5000/students \
#   -H "Content-Type: application/json" \
#   -d '{"name": "Mixed Student", "age": 25, "email": "mixed@example.com"}' &
# wait
# echo "✅ Mixed concurrent operations done."

# # Delete student
# echo "❌ Creating a Student for Deletion..."
# curl -s -X POST http://localhost:5000/students \
#   -H "Content-Type: application/json" \
#   -d '{
#         "name": "Delete Me",
#         "age": 30,
#         "email": "deleteme@example.com"
#       }' | tee delete_response.json | jq

# DELETE_ID=$(jq '.student.id' delete_response.json)

# echo "🗑️ Deleting Student with ID $DELETE_ID..."
# curl -s -X DELETE http://localhost:5000/students/$DELETE_ID | jq
# echo -e "\n"

# echo "🔎 Verifying Deletion (should return 404)..."
# curl -s -X GET http://localhost:5000/students/$DELETE_ID | jq
# echo -e "\n"

# rm delete_response.json

# # Final Student Count
# echo "📊 Final Student List:"
# curl -s -X GET http://localhost:5000/students -w "\nStatus: %{http_code}\n\n"

# echo "🎉 All Tests Complete!"


#!/bin/bash

echo "Running Student API Tests on http://localhost:5000"
echo "======================================="

# Health Check
echo "Health Check"
curl -s -X GET http://localhost:5000/health -w "\nStatus: %{http_code}\n\n"

# Create Students
echo "Creating Students"
curl -s -X POST http://localhost:5000/students \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "age": 20, "email": "john@example.com"}' \
  -w "\nStatus: %{http_code}\n\n"

curl -s -X POST http://localhost:5000/students \
  -H "Content-Type: application/json" \
  -d '{"name": "Jane Smith", "age": 22, "email": "jane@example.com", "interests": ["ML"], "achievements": ["Topper"], "courses": ["AI"]}' \
  -w "\nStatus: %{http_code}\n\n"

# Fetch All Students
echo "Fetching All Students"
curl -s -X GET http://localhost:5000/students -w "\nStatus: %{http_code}\n\n"

# Fetch Student by ID
echo "Fetching Student by ID (ID: 2)"
curl -s -X GET http://localhost:5000/students/2 | jq
echo -e "\n"

# Update Student
echo "Updating Student with ID 1"
curl -s -X PUT http://localhost:5000/students/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "Updated John", "age": 21}' \
  -w "\nStatus: %{http_code}\n\n"

# Generate Summary for Student
echo "Generating Summary for Student with ID 2"
curl -s -X GET http://localhost:5000/students/2/summary -w "\nStatus: %{http_code}\n\n"

# Concurrency Test: Create Multiple Students Simultaneously
echo "Creating 5 Students Concurrently..."
for i in {1..5}; do
  curl -s -X POST http://localhost:5000/students \
    -H "Content-Type: application/json" \
    -d "{\"name\": \"Concurrent Student $i\", \"age\": $((18+i)), \"email\": \"c$i@example.com\"}" \
    -w " [C$i: %{http_code}]" &
done
wait
echo -e "\nAll concurrent student creation requests completed.\n"

# Mixed Concurrent Operations
echo "Running Mixed Concurrent Operations..."
curl -s -X GET http://localhost:5000/students/2 &
curl -s -X PUT http://localhost:5000/students/2 \
  -H "Content-Type: application/json" \
  -d '{"email": "updated2@example.com"}' &
curl -s -X GET http://localhost:5000/students &
curl -s -X POST http://localhost:5000/students \
  -H "Content-Type: application/json" \
  -d '{"name": "Mixed Student", "age": 25, "email": "mixed@example.com"}' &
wait
echo "Mixed concurrent operations done."

# Delete Student
echo "Creating a Student for Deletion..."
curl -s -X POST http://localhost:5000/students \
  -H "Content-Type: application/json" \
  -d '{"name": "Delete Me", "age": 30, "email": "deleteme@example.com"}' | tee delete_response.json | jq

DELETE_ID=$(jq '.student.id' delete_response.json)

echo "Deleting Student with ID $DELETE_ID..."
curl -s -X DELETE http://localhost:5000/students/$DELETE_ID | jq
echo -e "\n"

echo "Verifying Deletion (expecting 404)..."
curl -s -X GET http://localhost:5000/students/$DELETE_ID | jq
echo -e "\n"

rm delete_response.json

# Final Student List
echo "Final Student List:"
curl -s -X GET http://localhost:5000/students -w "\nStatus: %{http_code}\n\n"

echo "All tests complete."
