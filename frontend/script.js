const API_URL = "http://localhost:8000/generate";

async function upload() {
  const fileInput = document.getElementById("fileInput");
  const status = document.getElementById("status");
  const output = document.getElementById("output");

  output.textContent = "";
  status.textContent = "";

  if (!fileInput.files.length) {
    status.textContent = "Please select a PDF file first.";
    return;
  }

  const file = fileInput.files[0];
  const formData = new FormData();
  formData.append("file", file);

  status.textContent = "Generating notes... this may take a moment.";

  try {
    const res = await fetch(API_URL, {
      method: "POST",
      body: formData,
    });

    const data = await res.json();

    if (data.error) {
      status.textContent = "Error: " + data.error;
      return;
    }

    status.textContent = "Done!";
    output.textContent = data.notes;
  } catch (err) {
    console.error(err);
    status.textContent = "An error occurred. Check the console for details.";
  }
}
