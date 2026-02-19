import profile1 from "./assets/nadia.jpg";
function Card() {
  return (
    <div>
      <img
        src={profile1}
        alt="profile picture"
        className="border border-solid border-gray-300 rounded-xl shadow-lg p-4 m-2 max-w-xs text-center inline-block w-32 h-32 rounded-full mx-auto"
      ></img>
      <h2>Bro code</h2>
      <p>I make youtube videos and play video games</p>
    </div>
  );
}

export default Card;
