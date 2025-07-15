async function fetchInfo() {
  const url = document.getElementById("url").value;
  const preview = document.getElementById("preview");
  const loader = document.getElementById("loader");
  const status = document.getElementById("status");

  preview.classList.add("hidden");
  status.innerText = "";
  loader.classList.remove("hidden");

  try {
    const res = await fetch("/info", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ url })
    });
    const data = await res.json();
    loader.classList.add("hidden");

    if (data.error) {
      status.innerText = "❌ Fehler: " + data.error;
      return;
    }

    document.getElementById("title").innerText = data.title;
    document.getElementById("channel").innerText = "📺 " + data.channel;
    document.getElementById("duration").innerText = `⏱️ Dauer: ${data.duration}s`;
    document.getElementById("thumbnail").src = data.thumbnail;
    document.getElementById("playlist").checked = !!data.is_playlist;

    preview.classList.remove("hidden");
  } catch (err) {
    loader.classList.add("hidden");
    status.innerText = "❌ Netzwerkfehler.";
  }
}

async function startDownload() {
  const url = document.getElementById("url").value;
  const format = document.getElementById("format").value;
  const quality = document.getElementById("quality").value;
  const playlist = document.getElementById("playlist").checked;
  const status = document.getElementById("status");
  const loader = document.getElementById("loader");

  loader.classList.remove("hidden");
  status.innerText = "";

  try {
    const res = await fetch("/download", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ url, format, quality, playlist })
    });
    const data = await res.json();
    loader.classList.add("hidden");

    if (data.download_url) {
      status.innerHTML = `✅ <a href="${data.download_url}">Download starten</a>`;
    } else {
      status.innerText = "❌ Fehler: " + (data.error || "Unbekannt");
    }
  } catch (err) {
    loader.classList.add("hidden");
    status.innerText = "❌ Serverfehler.";
  }
}
